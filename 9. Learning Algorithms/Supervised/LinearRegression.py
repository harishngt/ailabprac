pip install numpy scikit-learn matplotlib

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Simple dataset
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

# Create and train the linear regression model
model = LinearRegression()
model.fit(x, y)

# Make predictions
y_pred = model.predict(x)

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, y_pred, color='red', linewidth=2, label='Regression line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()

# Print the coefficients
print(f'Intercept: {model.intercept_}')
print(f'Slope: {model.coef_[0]}')

# Optionally, print the R^2 score
r2_score = model.score(x, y)
print(f'R^2 Score: {r2_score}')
