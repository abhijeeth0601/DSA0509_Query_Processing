import matplotlib.pyplot as plt
import numpy as np

# Sample Data
np.random.seed(42)

# Generate random data for three groups
group_1_heights = np.random.normal(160, 10, 30)
group_1_weights = np.random.normal(60, 5, 30)

group_2_heights = np.random.normal(170, 8, 30)
group_2_weights = np.random.normal(70, 6, 30)

group_3_heights = np.random.normal(155, 12, 30)
group_3_weights = np.random.normal(50, 8, 30)

# Plotting the scatter graph for three different groups
plt.scatter(group_1_heights, group_1_weights, color='blue',
            label='Group 1', alpha=0.7, edgecolor='black')
plt.scatter(group_2_heights, group_2_weights, color='green',
            label='Group 2', alpha=0.7, edgecolor='black')
plt.scatter(group_3_heights, group_3_weights, color='red',
            label='Group 3', alpha=0.7, edgecolor='black')

# Adding labels and title
plt.title('Scatter Plot: Heights vs Weights for Three Groups')
plt.xlabel('Heights (cm)')
plt.ylabel('Weights (kg)')

# Adding legend
plt.legend()

# Display the plot
plt.show()
