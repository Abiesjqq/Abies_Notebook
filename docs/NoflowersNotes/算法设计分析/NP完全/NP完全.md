
## Some NP hard problems

### SAT (Boolean Satisfiability Problem)

Given a CNF formula $\phi$, decide if it has a value assignment to make it true.

!!! remarks "Note"
    The knowledge of CNF and value assignment was learnt in Discrete Math, we gonna skip their introductions.

### Vertex Cover Problem

Given an _undirected_ graph $G$, a subset of vertices is a **vertex cover** if it contains at least one point of every edge.

The problem is to decide if the graph has a vertex cover of size $k$ for a given $k$.

### Independent Set Problem

Given an _undirected_ graph $G$, a subset of vertices is a **independent set** if there doesn't exist any edge between toe vertices.

The problem is to decide if the graph has a independent set of size $k$ for a given $k$.

!!! remarks "Denote in Matroid theorem"
    Find the maximum independent set in a given matroid $M = (E, \mathcal{I})$.

### Subset Sum Problem

Given a collection of integers $S = \{a_1, \ldots, a_n\}$, and $k \in \mathbb{Z}^+$, decide whether there exists a subset $T$ of $S$ that $\displaystyle \sum_{a \in T}a = k$.

### Hamiltonian Path Problem

A Hamiltonian path is a path in a undirected graph that pass through each vertex exactly once.

The problem is to decide whether a graph has a Hamiltonian path.

## Decision Problem and Turing Machine

### Decision problem

A decision problem is a function $f: \Sigma^* \to \{0, 1\}$

A decision problem contains:  
- Alphabet $\Sigma$, for example $\Sigma = \{0, 1\}$  
- $\displaystyle \Sigma^* = \bigcup_{n = 0}^\infty \Sigma^n$, all the strings with all length (we've discussed in discrete math)  
- $x \in \Sigma^*$, we can tell $f(x) = 1$ or $f(x) = 0$.

### Turning Machine

A turning machine contains:  
- A Tape: a infinite belt with each cell containing one alphabet.  
- A moving head pointing at a cell of the tape.  
- Two set: $\Sigma$ the alphabet and $Q$ the set of states, $Q$ includes a start state $q_{\mathrm{start}}$ and two halting states $q_{\mathrm{acc}}, q_{\mathrm{rej}}$.  
- A transition function: $\delta: Q \times \Sigma \to Q \times \Sigma \times \{L, R\}$

The working logic:

The turning machine starts from loading input onto the tape and moving head to the first cell of the tape with state $q_{\mathrm{start}}$.  
When it reaches one halting state, it will terminate and accept/reject the string.  
The output of TM is the content on the tape.

We have the **conclusion**: Whatever can be computed in polynomial time by a computer program or an algorithm can also be computed
in polynomial time by a Turing machine.

## Problems on TM

### Complexity classes

**P**

A turning machine $\mathcal{A}$ is a polynomial time TM if there exists a polynomial $p(x)$ such that $\mathcal{A}$ always terminates within $p(\operatorname{len}(x))$ steps on input $x$. 

A decision problem $f$ is in **P** iff there exists a polynomial time TM $\mathcal{A}$ that $\mathcal{A}$ accepts iff $f(x) = 1$ 

**NP**

Problems whose _yes_ instances can be efficiently verified if _hints_ are given, but they are not in **P** (Mostly if we construct a true case, naturally the problem gets true, and it is hard to prove false)

A decision problem is in **NP** iff there exists a polynomial $p$ and a poly-time TM $\mathcal{A}$ such that  
- If $f(x) = 1$, then there exists $y \in \Sigma^*$ with $\operatorname{len}(y) \leq q(\operatorname{len}(x))$, we have $\mathcal{A}$ accepts input $(x, y)$  
- If $f(x) = 0$, then for all $y \in \Sigma^*$ with $\operatorname{len}(y) \leq p(\operatorname{len}(x))$, we have $\mathcal{A}$ rejects the input $(x, y)$

The string $y$ is called a certificate.

SAT, VertexCover, IndependentSet, SubsetSum, HamiltonianPath are all in **NP**.

!!! remarks "An example to show SAT is in NP"

    Let $\mathcal{A}$:

    Accept if $x$ does encode a CNF $\phi$ and $y$ encodes an assignment that makes $phi$ be true. 
    Reject if $x$ doesn't encode a CNF $\phi$ or $y$ does not encode an assignment. 

Easily we can get **P** $\subseteq$ **NP**.

Problem still exists that, **is P equals NP**? Most researches believes no.

### Karp Reduction

A decision problem $f$ Karp reduce to $g$ if there exists a poly-time TM $\mathcal{A}$ such that:  
- $\mathcal{A}$ outputs a _yes_ instance of $g$ if input a _yes_ instance of $f$  
- $\mathcal{A}$ outputs a _no_ instance of $g$ if input a _no_ instance of $f$  

We denote it by $f \leq_k g$. It shows that $f$ is essentially a special case of $g$

We have such conclusions:

$$
\begin{aligned}
    \text{SAT} \leq_k &3\text{SAT} \leq_k \text{Independent Set} \leq_k \text{Vertex Cover} \leq_k \text{Subset Sum} \\
    &3\text{SAT} \leq_k \text{Hamiltonian Path}
\end{aligned}
$$

### NP-Hard and NP-Complete

A decision problem $f$ is **NP-hard** if for all $g \in$ NP, $g \leq_k f$;  
A decision problem $f$ is **NP-complete** if $f \in$ NP and for all $g \in$ NP, $g \leq_k f$

**Cook-Levin Theorem** tells us that SAT is NP-Complete. (To be completed...) (a CNF formula is sufficient to simulate the execution of a Turing Machine!)

So the problems of the inequality chain above are all NP-complete!

We have:

Solving NP-complete problems implies P $=$ NP;  
If P $\neq$ NP, then there exists NP problems that are nether P nor NP-complete. (Ladner’s Theorem)

### How to prove a problem is NP complete?

1. prove $f \in$ NP  
2. find an NP-complete problem $g$ and prove $g \leq_k f$$$ (Prove NP hard) (Namely, prove $x$ is yes $\Rightarrow y$ is yes; $y$ is yes $\Rightarrow x$ is yes)

## Other NP complete problems

### Subset Sum

**Partition+**

Given a collection of _positive_ integers $S$, decide if there is a partition of it $A, B$, such that $\sum_{a \in A}a = \sum_{b \in B}b$

### Hamiltonian Path

**Directed Hamiltonian Path**

Hamiltonian path on a directed graph

!!! remarks "3SAT $\leq_k$ Directed Hamiltonian Path"

    好多图，先不搞了

!!! remarks "Directed Hamiltonian Path $\leq_k$ Hamiltonian Path"

    也好多图 T^T

**Hamiltonian Cycle**

图图图

### Dominating Set

Decide whether a undirected graph has a dominating set of size $k$

!!! remarks "Dominating set and vertex cover"

To be completed

## NP hard Optimization Problem