## Recurrent NN

### Forward

$$
\begin{cases}
    \displaystyle h_t = f_W(h_{t - 1}, x_t) \\
    \displaystyle y_t = f_{W_hy}(h_t)
\end{cases}
$$

### Backpropagation

Only backpropagate for some smaller number of steps.