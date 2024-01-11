import matplotlib.pyplot as plt
import numpy as np

# Set a seed for reproducibility
np.random.seed(42)

# Generate random data for X and Y
num_points = 50
x_values = np.random.rand(num_points)
y_values = np.random.rand(num_points)

# Plotting the scatter graph with empty circles
plt.scatter(x_values, y_values, color='blue', alpha=0.7,
            edgecolor='black', marker='o', facecolor='none')

# Adding labels and title
plt.title('Scatter Plot with Empty Circles')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()
