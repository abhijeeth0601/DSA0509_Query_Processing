import numpy as np
import matplotlib.pyplot as plt

# Sample Data
categories = ['Category 1', 'Category 2',
              'Category 3', 'Category 4', 'Category 5']
means_men = np.array([22, 30, 35, 35, 26])
means_women = np.array([25, 32, 30, 35, 29])
std_dev_men = np.array([4, 3, 4, 1, 5])
std_dev_women = np.array([3, 5, 2, 3, 3])

# Plotting
fig, ax = plt.subplots()

# Plotting Men's bars
bars_men = ax.bar(categories, means_men, yerr=std_dev_men,
                  label='Men', color='blue', alpha=0.7, capsize=5)

# Plotting Women's bars on top of Men's bars
bars_women = ax.bar(categories, means_women, bottom=means_men,
                    yerr=std_dev_women, label='Women', color='orange', alpha=0.7, capsize=5)

# Adding labels and title
ax.set_xlabel('Categories')
ax.set_ylabel('Means')
ax.set_title('Stacked Bar Plot with Error Bars')
ax.legend()

# Display the plot
plt.show()
