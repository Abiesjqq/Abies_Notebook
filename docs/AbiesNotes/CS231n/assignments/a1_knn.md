## Compute Distances

### Two Loops

Implement the function compute_distances_two_loops that uses a (very inefficient) double loop over all pairs of (test, train) examples and computes the distance matrix one element at a time.

If there are Ntr training examples and Nte test examples, this stage should result in a Nte x Ntr matrix where each element (i,j) is the distance between the i-th test and j-th train example.

```py
def compute_distances_two_loops(self, X):
    """
    Inputs:
    - X: A numpy array of shape (num_test, D) containing test data.

    Returns:
    - dists: A numpy array of shape (num_test, num_train) where dists[i, j]
      is the Euclidean distance between the ith test point and the jth training
      point.
    """
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in range(num_test):
        for j in range(num_train):
            dists[i, j] = np.sqrt(np.sum(np.square(self.X_train[j, :] - X[i, :])))

    return dists
```

### One Loop

```py
def compute_distances_one_loop(self, X):
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in range(num_test):
        dists[i, :] = np.sqrt(np.sum(np.square(self.X_train - X[i, :]), axis=1))

    return dists
```

### No Loops

Principles:

$$\|\mathbf{x}-\mathbf{y}\|=\|\mathbf{x}\|^2+\|\mathbf{y}\|^2-2\mathbf{x}^T \mathbf{y}$$

```py
def compute_distances_no_loops(self, X):
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train))

    M = -2 * np.dot(X, self.X_train.T)
    M_train = np.array([np.sum(np.square(self.X_train), axis=1).T])
    M_test = np.array([np.sum(np.square(X))]).T
    dists = np.sqrt(M + M_train + M_test)

    return dists
```

## Predict Labels

```py
def predict_labels(self, dists, k=1):
    """
    Given a matrix of distances between test points and training points,
    predict a label for each test point.

    Inputs:
    - dists: A numpy array of shape (num_test, num_train) where dists[i, j]
        gives the distance between the ith test point and the jth training point.

    Returns:
    - y_pred: A numpy array of shape (num_test,) containing predicted labels
      for the test data, where y_pred[i] is the predicted label for test point X[i].
    """

    num_test = dists.shape[0]
    y_pred = np.zeros(num_test)

    for i in range(num_test):
        closest_y = []

        row = dists[i, :]
        sorted_indices = np.argsort(row)  # Indices that sort the distances (small to large)

        # Pick the labels of the k nearest neighbors
        for index in range(k):
            closest_y.append(self.y_train[sorted_indices[index]])

        # Count the occurrences of each label among the k nearest neighbors
        counts = {}
        for element in closest_y:
            if element not in counts:
                counts[element] = 1
            else:
                counts[element] += 1

        # Determine final label by majority vote
        label = 0
        for key in counts:
            if label not in counts:            # If label hasn't been assigned yet
                label = key
            if counts[key] > counts[label]:    # Found a label with higher count
                label = key
            if counts[key] == counts[label] and key < label:
                label = key

        y_pred[i] = label

    return y_pred

```

## Other Operations

### Subsample the Data

Subsample the data for more efficient code execution in this exercise.

```py
# Pick out the first 5000 training samples
num_training = 5000
mask = list(range(num_training))
X_train = X_train[mask]
y_train = y_train[mask]

# Pick out the first 500 testing samples
num_test = 500
mask = list(range(num_test))
X_test = X_test[mask]
y_test = y_test[mask]

# Reshape the image data into rows
X_train = np.reshape(X_train, (X_train.shape[0], -1))
X_test = np.reshape(X_test, (X_test.shape[0], -1))
print(X_train.shape, X_test.shape)
```

### Cross-validation

```py
num_folds = 5
k_choices = [1, 3, 5, 8, 10, 12, 15, 20, 50, 100]

X_train_folds = []
y_train_folds = []
X_train_folds = np.array_split(X_train, num_folds)
y_train_folds = np.array_split(y_train, num_folds)

k_to_accuracies = {}

for k in k_choices:
    for i in range(num_folds):
        validation_X = X_train_folds[i]
        validation_y = y_train_folds[i]
        train_X = np.concatenate(X_train_folds[:i] + X_train_folds[i + 1:])
        train_y = np.concatenate(y_train_folds[:i] + y_train_folds[i + 1:])

        Classifier = KNearestNeighbor()
        Classifier.train(train_X, train_y)
        y_prediction = Classifier.predict_labels(validation_X, k=k)

        NumCorrect = np.sum(y_prediction == validation_y)
        acc = float(NumCorrect) / len(validation_X)
        if i == 0:
            k_to_accuracies[k] = []
        k_to_accuracies[k].append(acc)

# Print out the computed accuracies
for k in sorted(k_to_accuracies):
    for accuracy in k_to_accuracies[k]:
        print('k = %d, accuracy = %f' % (k, accuracy))

```