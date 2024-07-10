import numpy as np

# Given data points (x, y)
x = np.array([1, 2, 3])
y = np.array([2, 5, 7])

# Initializing parameters
m = 0.0
c = 0.0

# Learning rate
alpha = 0.01

# Number of iterations
iterations = 1000

# Gradient Descent Algorithm
for i in range(iterations):
    # Predictions
    y_pred = m * x + c

    # Calculate the error
    error = ((y_pred - y) ** 2).sum()

    # Calculate gradients
    dm = (2 * (y_pred - y) * x).sum()
    dc = (2 * (y_pred - y)).sum()

    # Update parameters
    m -= alpha * dm
    c -= alpha * dc

    # Print the error every 100 iterations
    if i % 100 == 0:
        print(f"Iteration {i + 1}, Error: {error}, m: {m}, c: {c}")

# Final parameters
print(f"Final parameters: m = {m}, c = {c}")