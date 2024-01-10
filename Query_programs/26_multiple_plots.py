import matplotlib.pyplot as plt
import numpy as np

# Generating data for plots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Creating multiple plots
fig, axs = plt.subplots(2)  # Creating two subplots stacked vertically
fig.suptitle('Multiple Plots')  # Adding a title for the entire figure

# Plotting on the first subplot (upper plot)
axs[0].plot(x, y1, label='Sine', color='blue')
# Adding a label for the y-axis of the first subplot
axs[0].set_ylabel('Sine Function')
axs[0].legend()  # Adding legend to the first subplot

# Plotting on the second subplot (lower plot)
axs[1].plot(x, y2, label='Cosine', color='red')
# Adding a label for the x-axis of the second subplot
axs[1].set_xlabel('X-axis')
# Adding a label for the y-axis of the second subplot
axs[1].set_ylabel('Cosine Function')
axs[1].legend()  # Adding legend to the second subplot

# Adjusting layout
plt.tight_layout()

# Displaying the plot
plt.show()
