# SingleVariableLinearRegression
This project implements the Gradient Descent algorithm for linear regression using Python and NumPy. 

The code initializes parameters \( m \) (slope) and \( c \) (intercept), defines a learning rate \( \alpha \), and specifies the number of iterations for training. It iteratively updates \( m \) and \( c \) to minimize the Mean Squared Error (MSE) between predicted and actual values. The algorithm computes gradients using the derivative of the MSE with respect to \( m \) and \( c \), and adjusts \( m \) and \( c \) in the opposite direction of the gradient.

The main components include:
- Initialization of parameters \( m \) and \( c \)
- Looping through iterations to:
  - Compute predictions
  - Calculate errors
  - Compute gradients
  - Update parameters \( m \) and \( c \)
  - Print errors periodically
- Displaying the final values of \( m \) and \( c \)

This implementation serves as a fundamental exercise in applying Gradient Descent for optimizing linear regression models, demonstrating the core principles of parameter optimization in machine learning.
