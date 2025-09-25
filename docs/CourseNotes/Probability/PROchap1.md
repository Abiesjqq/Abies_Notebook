## 事件概念

- 随机试验：对随机现象的试验
- 样本空间：所有可能结果的集合
- 样本点：一个结果
- 随机事件：样本空间的子集
- 基本事件：只有一个样本点的随机事件
- 事件发生：结果包含于事件
- 必然事件：全集
- 不可能事件：空集

## 事件运算

- 和事件：$A\cup B$
- 积事件：$A\cap B=AB$
- 互不相容（互斥）：$A\cap B=\varnothing$
- 逆事件（对立事件）：$A\cup B=S\,\text{and}\, A\cap B=\varnothing$
- 差事件：$A-B$

## 频率与概率基本概念

- 频数：n 次试验中发生次数
- 频率：n 次中频数/n 的比值
- 概率：频率的极限
- 古典概型：有限个样本点，等概率
- 条件概率：$P(A|B)$表示 B 发生的条件下 A 发生的概率
- 先验概率：贝叶斯公式中$P(B_j)$
- 后验概率：贝叶斯公式中$P(B_j|A)$
- 相互独立：$P(AB)=P(A)P(B)$，积事件的概率等于概率的积
- 独立试验：试验结果互不影响
- 重复试验：相同条件下的试验

概率有可列可加性，如果有一列两两互不相容的事件 \(A_1, A_2, A_3, \dots\)，那么

\[
P\Bigl(\bigcup_{i=1}^{+\infty} A_i\Bigr) = \sum_{i=1}^{+\infty} P(A_i).
\]

并非所有概率都能直接相加，比如线段上单点的概率都为 0，但整个区间的概率为 1。

## 基本公式

**德摩根律：**

$$\overline{\bigcup_{j=1}^n A_j}=\bigcap_{j=1}^n\overline{A_j}$$

$$\overline{\bigcap_{j=1}^n A_j}=\bigcup_{j=1}^n\overline{A_j}$$

**差集的概率运算：**

$$P(A-B)=P(A)-P(AB)$$

**容斥原理：**

至少一个事件发生 = 所有奇数个事件发生概率求和 - 所有偶数事件发生概率求和

$$P\left(\bigcup_{j=1}^n A_j\right)=\sum_{j=1}^n P(A_j)-\sum_{i<j}P(A_i A_j)+\sum_{i<j<k}P(A_i A_j A_k)-\cdots +(-1)^{n-1}P(A_1 A_2\cdots A_n)$$

**条件概率乘法：**

$$P(AB)=P(A)P(A|B)=P(B)P(B|A)$$

**全概率公式：**

$B_1,B_2\cdots B_n$是整个样本空间的划分，则

$$P(A)=\sum_{j=1}^n P(B_j)P(A|B_j)$$

**贝叶斯公式：**

$B_1,B_2\cdots B_n$是整个样本空间的划分，则

$$P(B_k|A)=\frac{P(B_k A)}{P(A)}=\frac{P(B_k)P(A|B_k)}{\displaystyle \sum_{j=1}^n P(B_j)P(A|B_j)}$$
