# Randomized Algorithms

Efficient randomized algorithms only need to yield the correct answer with high probability.

## Examples

### Hiring Problem

Hire an office assistant from headhunter. Interview a different applicant per day for $N$ days. Interviewing cost $C_i <<$ hiring cost $C_h$.

Assume $M$ people are hired, then the total cost is $O(NC_i+MC_h)$.

!!! remarks "Naive solution"

    Traverse all candidate, and update the best choice.

    ---

    ```c
    int Hiring(EventType C[], int N) {
        int Best = 0;
        int BestQ = the quality of best candidate;
        for (i = 1; i <= N; i++) {
            Qi = interview(i);  // cost: Ci
            if (Qi > BestQ) {
                BestQ = Qi;  // update best candidate
                Best = i;
                hire(i);  // cost: Ch
            }
        }
        return Best;
    }
    ```

    Worst case: The candidates come in increasing quality order, where the total time is $O(NC_h)$.

!!! remarks "Randomized algorithms"

    Permute the list of candidates randomly.

    ---

    Assume candidates arrive in random order. Let $X$ denote the number of hires. $X_i$ denote whether candidiate $i$ is hired, i.e., $X_i=1$ if candidate $i$ is hired, and 0 if not.

    From the difinition, $X=\sum_{i=1}^N X_i$, and each $X_i$ has a probability to be 1. The expectance of $X$ is:

    $$E(X)=\sum_{i=1}^N E(X_i)=\sum_{i=1}^N \frac{1}{i}=\ln N+O(1).$$

    Therefore, the total time is $O(C_h\ln N+NC_i)$.

    ```c
    int RandomizedHiring(EventType C[], int N) {
        int Best = 0;
        int BestQ = the quality of best candidate;

        // bad: takes time
        randomly permute the list of candidates;

        // good: no need to assume that candidates are presented in random order
        for (i = 1; i <= N; i++) {
            Qi = interview(i);  // cost: Ci
            if (Qi > BestQ) {
                BestQ = Qi;
                Best = i;
                hire(i);  // cost: Ch
            }
        }
    }
    ```

        !!! remarks "Randomized Permutation Algorithm"

            Consider permuting array $A$.

            Assign each element $A_i$ a random priority $P_i$, and sort the array.

!!! remarks "Online Hiring Algorithm"

    Examine the first $k$ candidates to establish a benchmark (the best quality observed so far). Then, starting from candidate $k+1$, hire the first candidate whose quality exceeds this benchmark.

    ---

    ```c
    int OnlineHiring(EventType C[], int N, int k) {
        int Best = N;
        int BestQ = -INF;
        for (i = 1; i <= k; i++) {
            Qi = interview(i);
            if (Qi > BestQ)
                BestQ = Qi;
        }
        for (i = k + 1; i <= N; i++) {
            Qi = interview(i);
            if (Qi > BestQ) {
                Best = i;
                break;
            }
        }
        return Best;
    }
    ```

    Let $S_i$ denote the event that the $i$-th applicant is the best. $S_i$ requires the best one is at position $i$ ($P(A)=1/N$) and no one at positions $k+1$ ~ $i–1$ are hired (i.e., the maximum value of first $i-1$ applicant appears in the first $k$ position, $P(B)=k/(i-1)$).

    Probility of $S_i$:

    $$P(S_i)=P(A\cap B)=P(A)P(B)=\frac{k}{N(i-1)}$$

    The probability we hire the best qualified candidate for a given $k$:

    $$P(S)=\sum_{i=k+1}^N P(S_i)=\sum_{i=k+1}^N \frac{k}{N(i-1)} =\frac{k}{N}\sum_{i=k+1}^N\frac{1}{i}.$$

    Since

    $$\ln\left(\frac{N}{k}\right)=\int_k^N\frac{1}{x}\mathrm{d}x\le \sum_{i=k+1}^N\frac{1}{i} \le \int_{k-1}^{N-1}\frac{1}{x}\mathrm{d}x = \ln\left(\frac{N-1}{k-1}\right),$$

    the range of $P(S)$ satisfies:

    $$\frac{k}{N}\ln\left(\frac{N}{k}\right) \le P(S) \le \frac{k}{N}\ln\left(\frac{N-1}{k-1}\right).$$

### Quicksort

!!! remarks "Deterministic Quicksort"

    Time complexity:

    - Worst case: $O(N^2)$;
    - Average case: $O(N\log N)$.

    The key is to always always select better pivot before recursions.

    **Central splitter**: the pivot that divides the set so that each side contains at least $n/4$.

!!! remarks "Randomized Quicksort"

    _How about choosing the pivot uniformly at random?_

    The time complexity becomes $O(N\log N)$.

    !!! normal-comment "Proof"

        If randomly choosing pivot, the probability of pick central splitter is 1/2 (since the length of satisfied interval is $N/2$), thus the expected number of iterations needed until finding a central spiltter is 2.

        Def size of subproblem as **type $j$**: the subproblem $S$ is of type $j$ if 
        
        $$N\left(\frac{3}{4}\right)^{j+1}\le |S|\le N\left(\frac{3}{4}\right)^j.$$

        Type $j$ subproblems do not overlap, therefore the number of type $j$ subproblems is at most

        $$\frac{N}{N(3/4)^{j+1}}=\left(\frac{4}{3}\right)^{j+1}.$$

        In each subproblem, the algorithm scans its elements and compare with pivot. Thus the time of every single type $j$ subproblem is $O(N(3/4)^j)$, and time of all type $j$ subproblems (one layer of the whole problem) is 

        $$E[T_{type j}]=O\left(N\left(\frac{3}{4}\right)^j\right)\times \left(\frac{4}{3}\right)^{j+1}=O(N).$$

        When divide the current problem into size 1 subproblem, the partition terminates. Moving down to the next layer makes the size of subproblem decrease into 3/4. Therefore when $N(3/4)^j=1$ it terminates, i.e. the number of different types is $n_j=\log_{4/3}N=O(\log N).$

        The total time complexity:

        $$T=\text{Time\,of\,each\,layer}\times \text{\#Layers}=O(N)\times O(\log N)=O(N\log N).$$


### Global Min Cut

Given a connected, undirected graph $G = (V, E)$, find a cut $(A, B)$ of minimum cardinality.

**Contraction algorithm**: Pick an edge $e=(u,v)$ uniformly at random. Contract edge $e$ (replace $u$ and $v$ by single new super-node $w$, preserve edges, updating endpoints of $u$ and $v$ to $w$, keep parallel edges and delete self-loops.) Repeat ultil graph has just two nodes. Return the cut.

The contraction algorithm returns a min cut with prob $\ge 2 / n^2$.

## Homework

!!! examples "E.g. T/F"

    Consider the randomized quicksort. We have proved that it runs in $O(n\log n)$ time in expectation even for the worst input. Is the following statement true of false?There exists some good inputs on which the expected running time of randomized quicksort is O(n) where n is the input size.

    (F)

    ---

    Let $T(n)$ be the running time of quicksort on an input of size $n$. We already know that $T(n)$ is a random variable whose value depends on the random choices of quicksort, and that the expectation of $T(n)$ is $O(n \log n)$. Is the following statement true or false? The minimum possible value of $T(n)$ can be as small as $\Theta(n)$, and the maximum possible value can be as large as $\Theta(n^2)$.

    (F)
