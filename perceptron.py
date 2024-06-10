import numpy as np

def perceptron_classification(X, y, weights, theta, num_iterations, learning_rate):
    # Training
    for _ in range(num_iterations):
        for i in range(len(X)):
            # Calculate the dot product of weights and input features
            y_pred = np.dot(X[i], weights)
            
            # Update weights if prediction is incorrect
            if y_pred <= theta and y[i] == 1:
                weights += learning_rate * X[i]
            elif y_pred > theta and y[i] == -1:
                weights -= learning_rate * X[i]
            print(y_pred)
    return weights

# User inputs
X = np.array([[1, 1], [0.5, 3], [2, 5], [2, 1], [3, 3], [4, 2]])
y = np.array([1, 1, 1, -1, -1, -1])
weights = np.array([-1, 1], dtype=float)

num_iterations = int(input("Enter the number of iterations: "))
learning_rate = float(input("Enter the learning rate (e.g., 0.1): "))
theta = float(input("Enter the threshold value (e.g., 0.5): "))

# Get weights
weights = perceptron_classification(X, y, weights, theta, num_iterations, learning_rate)
print("Weights after", num_iterations, "iterations:", weights)
