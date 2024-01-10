import matplotlib.pyplot as plt

# Reading data from the text file
with open('test.txt', 'r') as file:
    data = file.readlines()

# Extracting x and y values
x = []
y = []
for line in data:
    values = line.split()
    x.append(int(values[0]))
    y.append(int(values[1]))

# Plotting the line
plt.plot(x, y)

# Adding labels to the x-axis and y-axis, and a title
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Line Plot from test.txt')

# Displaying the plot
plt.show()
