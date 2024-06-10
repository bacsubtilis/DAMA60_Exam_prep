import numpy as np
from fractions import Fraction

def hinge_loss(margins):
    return np.maximum(0, 1 - margins)


def svm_gradient_descent(X, y, w, b, lr, C, n_iter):
    """
    SVM with Gradient Descent.

    Parameters:
    X : numpy array
        Feature matrix of shape (m, n), where m is the number of samples and n is the number of features.
    y : numpy array
        Target labels of shape (m,).
    w : numpy array
        Initial weights of shape (n,).
    b : float
        Initial bias.
    lr : float
        Learning rate.
    C : float
        Regularization parameter.
    n_iter : int
        Number of iterations.

    Returns:
    weights_list : list of numpy arrays
        List containing the updated weights after each iteration.
    bias_list : list of floats
        List containing the updated bias after each iteration.
    predictions : list of strings
        List containing predictions ('o' for correct, 'x' for incorrect) after each iteration.
    """

    m = X.shape[0]
    weights_list = []
    bias_list = []
    predictions = []

    for _ in range(n_iter):
        # Compute margins
        margins = y * (np.dot(X, w) + b)

        # Compute hinge loss
        loss = hinge_loss(margins)
        
        # Compute predicitons before initial weight change
        preds = np.sign(np.dot(X, w) + b)

        # Compute gradients
        incorrect_indices = np.where(margins < 1)[0]
        w_gradient = - C * np.dot(y[incorrect_indices], X[incorrect_indices])
        b_gradient = - C * np.sum(y[incorrect_indices])

        # Update weights and bias
        w = w - lr * (w + w_gradient)
        b = b - lr * (b + b_gradient)

        # Append the updated weights and bias to the lists
        weights_list.append(w.copy())
        bias_list.append(b)

        # Update predictions list after weight change
        predictions.append(
            "".join(['o' if preds[i] == y[i] else 'x' for i in range(len(preds))]))

    return weights_list, bias_list, predictions


# Given data
X = np.array([[1, 1], [Fraction(1,2), 3], [2, 5], [2, 1], [3, 3], [4, 2]])
y = np.array([1, 1, 1, -1, -1, -1])

# Initialize weights and bias
w = np.array([-1, 0])
b = -1

# Set hyperparameters
lr = Fraction(1,4)
C = 2
n_iter = 2

# Train SVM using gradient descent
updated_weights, updated_bias, predictions = svm_gradient_descent(
    X, y, w, b, lr, C, n_iter)
for i in range(n_iter):
    print(f"Iteration {i+1}:")
    print("Updated weights:", [f"{num}/{den}" for num, den in [(f.numerator, f.denominator) for f in updated_weights[i]]])
    print("Updated bias:", updated_bias[i])
    print("Prediction:", predictions[i])
    print()
