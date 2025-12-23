## Examples

### Contention Resolution

### Global Min Cut

Given a connected, undirected graph $G = (V, E)$, find a cut $(A, B)$ of minimum cardinality. 

**Contraction algorithm**: Pick an edge $e=(u,v)$ uniformly at random. Contract edge $e$ (replace $u$ and $v$ by single new super-node $w$, preserve edges, updating endpoints of $u$ and $v$ to $w$, keep parallel edges and delete self-loops.) Repeat ultil graph has just two nodes. Return the cut.

The contraction algorithm returns a min cut with prob $\ge 2 / n^2$. 

??? normal-comment "Proof"

    To be supplemented.