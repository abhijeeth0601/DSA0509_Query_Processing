import matplotlib.pyplot as plt
import numpy as np

# Sample data
men_means = [22, 30, 35, 35, 26]
women_means = [25, 32, 30, 35, 29]

# Number of groups
N = len(men_means)

# Generating the indices for each group
ind = np.arange(N)

# Width of the bars
width = 0.35

# Creating the bar plot
plt.figure(figsize=(8, 6))
plt.bar(ind, men_means, width, label='Men')
plt.bar(ind + width, women_means, width, label='Women')

# Adding labels and title
plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(ind + width / 2, ('Group1', 'Group2', 'Group3', 'Group4', 'Group5'))
plt.legend()

# Displaying the plot
plt.tight_layout()
plt.show()
