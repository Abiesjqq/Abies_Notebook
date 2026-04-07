# JDBC食用指南

## 基本框架

JDBC是Java提供的用于连接和操作数据库的API。分为（加载驱动、）建立连接、创建对象语句、执行SQL、处理结果、关闭资源几个步骤。

数据库查询：

```java
// 建立连接
Connection conn = DriverManager.getConnection(url, user, password);

// 创建对象语句
String sql = "SELECT * FROM student";
PreparedStatement pstmt = conn.prepareStatement(sql);

// 执行SQL（查询）
ResultSet rs = pstmt.executeQuery();

// 处理结果
while (rs.next()) {
    int id = rs.getId("id");
    String name = rs.getString("name");
    System.out.println(id + name);
}

// 关闭资源
rs.close();
pstmt.close();
conn.close();
```

数据库插入/修改/删除：

```java
// 建立连接
Connection conn = DriverManager.getConnection(url, user, password);

// 创建对象语句
String sql = "INSERT INTO student (id, name) VALUES (?, ?)";
PreparedStatement pstmt = conn.prepareStatement(sql);
// 设置参数
pstmt.setInt(1, 1);
pstmt.setString(2, "Abies");

// 执行SQL（插入/修改/删除）
int rows = pstmt.executeUpdate();

// 处理结果
System.out.println(rows);

// 关闭资源
pstmt.close();
conn.close();
```

## 控制事务

设置`conn.setAutoCommit(false);`关闭自动提交。执行一组任务时，若成功则统一提交，否则全部回滚。整体框架为：

```java
setAutoCommit(false);

try { ... commit(); }
catch { rollback(); }
finally { close(); }
```

示例，尝试插入两条数据：

```java
Connection conn = DriverManager.getConnection(url, user, password);
conn.setAutoCommit(false);
PreparedStatement pstmt = null;

try {
    String sql = "INSERT INTO student (id,name) VALUES (?,?)";
    pstmt = conn.prepareStatement(sql);

    pstmt.setInt(1, 1);
    pstmt.setString(2, "Alice");
    pstmt.execuateUpdate();

    pstmt.setInt(1, 2);
    pstmt.setString(2, "Bob");
    pstmt.executeUpdate();

    conn.commit();
} catch (Exception e) {
    conn.rollback();
} finally {
    if (pstmt != null) {
        pstmt.close();
    }
    conn.close();
}
```

## 并发时加锁

执行并发操作时，可能因读写时序不一致导致冲突。此时，需要加锁来锁住数据库中的某些数据记录，当其他进程访问被锁住的记录时，需要等待其提交或回滚；当当前事务结束时，锁释放。加锁从`executeQuery`开始生效，相当于把普通操作变为原子操作。

最小改动：在SELECT语句后加`FOR UPDATE`。

示例：如果bookId书的库存大于零，则借一本书

```java
Connection conn = null;
PreparedStatement pstmt = null;
ResultSet rs = null;

try {
    conn = DriverManager.getConnection(url, user, password);
    conn.setAutoCommit(false);

    // 锁住这本书
    String lockSql = "SELECT stock FROM book WHERE book_id = ? FOR UPDATE";
    pstmt = conn.prepareStatement(lockSql);
    pstmt.setInt(1, bookId);
    rs = pstmt.executeQuery();

    if (!rs.next()) {
        throw new RuntimeException("图书不存在");
    }

    int stock = rs.getInt("stock");

    if (stock <= 0) {
        throw new RuntimeException("库存不足");
    }

    rs.close();
    pstmt.close();

    // 插入借书记录
    String borrowSql = "INSERT INTO borrow(card_id, book_id, borrow_time) VALUES (?, ?, ?)";
    pstmt = conn.prepareStatement(borrowSql);
    pstmt.setInt(1, cardId);
    pstmt.setInt(2, bookId);
    pstmt.setLong(3, borrowTime);
    pstmt.executeUpdate();
    pstmt.close();

    // 更新库存
    String updateSql = "UPDATE book SET stock = stock - 1 WHERE book_id = ?";
    pstmt = conn.prepareStatement(updateSql);
    pstmt.setInt(1, bookId);
    pstmt.executeUpdate();

    conn.commit();
} catch (Exception e) {
    if (conn != null) conn.rollback();
    e.printStackTrace();
} finally {
    if (rs != null) rs.close();
    if (pstmt != null) pstmt.close();
    if (conn != null) conn.close();
}
```

## 图书管理系统注意事项

### storeBook函数

```java
@Override
public ApiResult storeBook(Book book) {
    Connection conn = connector.getConn();
    String sql = "INSERT INTO book (category, title, press, publish_year, author, price, stock) VALUES (?, ?, ?, ?, ?, ?, ?)";
    try (PreparedStatement pstmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {  // pstmt写在try()中，能自动调用析构函数，不用自己写close
        pstmt.setString(1, book.getCategory());
        pstmt.setString(2, book.getTitle());
        pstmt.setString(3, book.getPress());
        pstmt.setInt(4, book.getPublishYear());
        pstmt.setString(5, book.getAuthor());
        pstmt.setDouble(6, book.getPrice());
        pstmt.setInt(7, book.getStock());

        int affectedRows = pstmt.executeUpdate();
        if (affectedRows != 1) {  // 检查插入是不是只插入了一行，这个是否必要？
            rollback(conn);
            return new ApiResult (false, "Failed to store book");
        }

        try (ResultSet generatedKeys = pstmt.getGeneratedKeys()) {  // 插入后形成book_id，写回book中作为主键
            if (generatedKeys.next()) {
                book.setBookId(generatedKeys,getInt(1));
            } else {
                rollback(conn);
                return new ApiResult(false, "Failed to fetch generated book id");
            }
        }

        commit(conn);
        return new ApiResult(true, null);
    } catch (Exception e) {
        rollback(conn);
        return new ApiResult(false, e.getMessage());
    }
}
```

### incBookStock函数

```java
@Override
public ApiResult incBookStock(int bookId, int deltaStock) {
    Connection conn = connector.getConn();
    String selectSql = "SELECT stock FROM book WHERE book_id = ? FOR UPDATE";  // FOR UPDATE加锁，将SELECT变为原子操作，防止并行时读写不一致导致冲突
    String updateSql = "UPDATE book SET stock = stock + ? WHERE book_id = ?";
    
    try (PreparedStatement pstmtSelect = conn.prepareStatement(selectSql)) {
        pstmtSelect.setInt(1, bookId);
        ResultSet rs = pstmtSelect.executeQuery();
        if (!rs.next()) {  // 用于检查是否有返回结果
            rollback(conn);
            return new ApiResult(false, "Invalid book id");
        }

        // 不用检查返回结果是不是大于一行，这个在插入时检查
        int stock = rs.getInt("stock");  // 如果上一条成功，已经指在第一行返回结果前，直接getInt
        if (stock + deltaStock < 0) {  // 注意deltaStock可能为负数！检查更新后stock是不是为负
            rollback(conn);
            return new ApiResult(false, "Result stock cannot be negative");
        }

        try (PreparedStatement pstmtUpdate = conn.prepareStatement(updateSql)) {
            pstmtUpdate.setInt(1, deltaStock);
            pstmtUpdate.setInt(2, bookId);
            int affectedRows = pstmtUpdate.executeUpdate();
            if (affectedRows != 1) {
                rollback(conn);
                return new ApiResult(false, "Failed to update book stock");
            }

            conn.commit();
            return new ApiResult(true, null);
        }
    } catch(Exception e) {  // 内层try失败，同样会跳到外层的catch，因此只需写一个catch
        rollback(conn);
        return new ApiResult(false, e.getMessage());
    }
}
```

### storeBook（多本书）函数

```java
@Override
public ApiResult storeBook(List<Book> books) {
    Connection conn = connector.getConn();
    String sql = "INSERT INTO book (category, title, press, publish_year, author, price, stock) VALUES (?, ?, ?, ?, ?, ?, ?)";
    try (PreparedStatement pstmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
        for (Book book : books) {  // 注意要求，不能多次调用单本书的storeBook函数
            pstmt.setString(1, book.getCategory());
            pstmt.setString(2, book.getTitle());
            pstmt.setString(3, book.getPress());
            pstmt.setInt(4, book.getPublishYear());
            pstmt.setString(5, book.getAuthor());
            pstmt.setDouble(6, book.getPrice());
            pstmt.setInt(7, book.getStock());
            pstmt.addBatch();  // 加入批处理
        }

        int[] affectedRows = pstmt.executeBatch();  // 一次性执行批处理，自动“一次不成功则整体回滚”
        if (affectedRows.length != books.size()) {  // 检查插入总行数是否等于书的数量
            rollback(conn);
            return new ApiResult(false, "Failed to store books");
        }

        try (ResultSet generatedKeys = pstmt.getGeneratedKeys()) {  // 给每本书写回生成的id
            int idx = 0;
            while (generatedKeys.next() && idx < books.size()) {
                books.get(idx).setBookId(generatedKeys.getInt(1));
                idx++;
            }
            if (idx != books.size()) {
                rollback(conn);
                return new ApiResult(false, "Failed to fetch generated book ids");
            }
        }

        commit(conn);
        return new ApiResult(true, null);
    } catch (Exception e) {
        rollback(conn);
        return new ApiResult(false, e.getMessage());
    }
}
```


### removeBook函数

```java
@Override
public ApiResult removeBook(int bookId) {
    Connection conn = connector.getConn();
    String removeSql = "DELETE FROM book WHERE book_id = ?";
    String checkSql = "SELECT 1 FROM borrow WHERE book_id = ? AND return_time = 0";  // return_time=0表示未归还

    try (PreparedStatement pstmtCheck = conn.prepareStatement(checkSql)) {
        pstmtCheck.setInt(1, bookId);
        try (ResultSet rsCheck = pstmtCheck.executeQuery()) {  // ResultSet写在try中，避免手动调用close
            if (rsCheck.next()) {
                rollback(conn);
                return new ApiResult(false, "Book has unreturned borrow records");
            }
        }

        try (PreparedStatement pstmtRemove = conn.prepareStatement(removeSql)) {
            pstmtRemove.setInt(1, bookId);
            int affectedRows = pstmtRemove.executeUpdate();
            if (affectedRows != 1) {
                rollback(conn);
                return new ApiResult(false, "Invalid book id");
            }
        }
        
        commit(conn);
        return new ApiResult(true, null);
    } catch(Exception e) {
        rollback(conn);
        return new ApiResult(false, e.getMessage());
    }   
}
```