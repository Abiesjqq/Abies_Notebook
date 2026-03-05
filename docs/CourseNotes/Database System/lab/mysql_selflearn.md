```sql
use game;

create table player (
	id INT,
    name VARCHAR(100),
    level INT,
    exp INT DEFAULT 0,
    gold DECIMAL(10,2) DEFAULT 0
);

DESC player;

ALTER TABLE player MODIFY COLUMN level INT DEFAULT 1;
-- ALTER TABLE player MODIFY COLUMN name VARCHAR(200);
-- ALTER TABLE player RENAME COLUMN name to nick_name;
-- ALTER TABLE player ADD COLUMN last_login datetime;
-- ALTER table player drop column last_login;

INSERT INTO player VALUES (1,'Abies',1,1,1);
INSERT INTO player (id,name) VALUES (2,'x'), (3,'y');
INSERT INTO player (id,name,level) VALUES (4,'aa',4), (5,'ab',5);
-- INSERT INTO player (id,name,level,exp,gold) VALUES (2,'hi',1,1,1);
-- INSERT INTO player (id,name) VALUES (3,'x');

SET SQL_SAFE_UPDATES = 0;
UPDATE player SET exp = 0 WHERE id = 2;
UPDATE player SET exp = 0 WHERE name = 'y';
UPDATE player SET gold = 100;

DELETE FROM player WHERE name = 'Abies';

SELECT * FROM player;
SELECT * FROM player WHERE level > 1;
SELECT * FROM player WHERE level > 1 AND level < 5;
SELECT * FROM player WHERE level IN (1,3,5);
SELECT * FROM player WHERE level NOT BETWEEN 1 AND 10;
SELECT * FROM player WHERE exp IS null;
SELECT * FROM player WHERE name = '';

-- LIKE用于模糊查询，% 表示任意个字符，_ 表示任意一个字符
SELECT * FROM player WHERE name LIKE 'a%';

-- REGEXP使用正则表达式匹配
-- . 表示任意一个字符，^ 表示开头，$ 表示结尾
-- [abc] 表示其中任意一个字符，[a-z] 表示范围内任意一个字符，A|B 表示A或B
SELECT * FROM player WHERE name REGEXP '[a-z]';
SELECT * FROM player WHERE name REGEXP '^a.$';

-- ORDER BY 排序
SELECT * FROM player ORDER BY level; 
SELECT * FROM player ORDER BY level DESC, gold ASC;

-- 常用聚合函数：AVG(), COUNT(), MAX(), MIN(), SUM()
-- GROUP BY 分组，HAVING 分组后筛选, LIMIT 限制输出的数量或偏移量
SELECT COUNT(*) FROM player;
SELECT AVG(gold) FROM player;
SELECT gold,COUNT(*) FROM player GROUP BY gold;
SELECT gold,COUNT(gold) FROM player GROUP BY gold HAVING COUNT(gold) > 2;

-- DISTINCT 去重, UNION 合并查询结果（默认去重）
-- INTERSECT 取查询结果的交集，EXCEPT 取查询结果的差集
SELECT DISTINCT name FROM player;

SELECT * FROM player WHERE name REGEXP '[a-z]'
UNION
SELECT * FROM player WHERE level IN (1,3,5);

-- 子查询
SELECT * FROM player WHERE gold > (SELECT AVG(gold) FROM player);
SELECT gold, ROUND((SELECT AVG(gold) FROM player)) AS average,
	gold - ROUND((SELECT AVG(gold) FROM player)) AS diff
    FROM player;
    
create table new_player select * from player where level <= 1;
select * from new_player;
insert into new_player select * from player where level between 2 and 4;
select exists (select * from new_player where level > 5);

-- 表关联





-- DROP TABLE player;
```