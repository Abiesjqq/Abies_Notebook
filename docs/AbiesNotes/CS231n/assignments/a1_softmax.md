## Calculate Softmax Loss

### Naive computation

```py
def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    num_train = X.shape[0]
    num_class = W.shape[1]
    scores = X.dot(W)
    scores = np.exp(scores - np.max(scores))
    p = scores / np.sum(scores, axis=1).reshape(num_train, 1)

    for i in range(num_train):
        loss -= np.log(p[i][y[i]])
        for j in range(num_class):
            if j == y[i]:
                dW[:, j] += (p[i][j] - 1) * X[i].T
            else:
                dW[:, j] += p[i][j] * X[i].T
    loss /= num_train
    loss += reg * np.sum(W * W)

    dW /= num_train
    dW += 2 * reg * W
    return loss, dW
```