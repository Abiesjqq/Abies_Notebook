## Introduction

AI is categorized into three fields:

- ANI (Narrow): in a specific field
- AGI (General): human level intelligence
- ASI (Super): high-level and all-field intelligence

Relation of some terminologies: AI $\in$ ML $\in$ DL. (DL uses neural network, while ML can use other options, like SVM, forest, linear regression, etc.)

Kinds of ML problems:

- **Supervised learning**: given features and labels, predict label from new features. E.g., regression, classification, tagging, search, etc.
- **Unsupervised learning**: given unlabeled data, discover inherent patterns. E.g., clustering, generative models, etc.
- **Reinforcement learning**: Given rewards/penalties, autonomous agents learn policy by interacting with the environment. E.g., robotics, self-driving, etc.

## Supervised Learning

Core concepts:

- Data: good datasets are both large and highly diverse.

### Data

Divide the original dataset into three parts:

- Training set
- Validation set: used to perform initial testing of the model as it is being trained.
- Test set: used for the evaluation of the trained model.

#### Overfitting and Uderfitting

- Overfitting: memorizes the training set too closely.
- Underfitting: even cannot make good decision on training data.

Causes of overfitting:

- Training data doesn't adequately represent real-world data
- The model is too complex.

**_Q: How to detect overfitting?_**

Generalization curve: a plot of the model's performace

Occam's razor.

Regularization: With the goal of both fitting data well and making the model simple. Penalizing comlex models is one form of regularization.

Combine loss and complexity: minimize(loss + complexity).

## Neurons

### McCulloch Pitts Neuron

A McCulloch Pitts neuron: $y=f(g(x_i))=1 \text{ if } g(x_i)> \theta$, where $\theta$ is called threshold, and $g(x_i)$ can be weighted sum. 

E.g.:

- Perceptron learning: training a binary linear classifier (a perceptron).
- Linear separability: generally, $w^T x+b=0$ is a hyperplane in 2D spaces or above.

Solving XOR problem: Cannot separate the poits with a single line, but can use two (or multiple) lines.

### Sigmoid Neuron

Sigmoid function: smoother than 0-1 threshold function, continuous, and differentiable.

Use different parameters w and b (bias), can draw different shapes of sigmoid function.

Combine sigmoid functions, can get a "tower" function, or other arbitiry shapes.

### Layers of Neurons

## Gradient Descent

Learning rate schedule: startig with a larger step size for faster progress and gradually devreasing it into fine-tunne the parameters.

## Regularization

Dataset augmentation: uses pre-existiing data to create new data samplees that can improve model optimizaiton adn generalizability.

Early stopping: stop if the validation error has no improvement.

Dropout:temporarily remove a node and all is relevant connections resulting in a thinned network during training.

Ensamble methods:

Bagging:

Parameter sharing and tying:

Adding noise to the inputs:

L2 regulization:

