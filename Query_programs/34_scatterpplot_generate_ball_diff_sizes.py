import matplotlib.pyplot as plt
import numpy as np

# Set a seed for reproducibility
np.random.seed(42)

# Generate random data for X, Y, and sizes
num_points = 50
x_values = np.random.rand(num_points)
y_values = np.random.rand(num_points)
colors = np.random.rand(num_points, 3)
# Random sizes between 10 and 100
sizes = np.random.randint(10, 500, num_points)

# Plotting the scatter graph with balls of different sizes
plt.scatter(x_values, y_values, color=colors,
            alpha=0.7, s=sizes, edgecolor='black')

# Adding labels and title
plt.title('Scatter Plot with Balls of Different Sizes')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()
