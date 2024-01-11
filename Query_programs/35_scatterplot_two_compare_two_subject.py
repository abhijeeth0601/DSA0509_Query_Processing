import matplotlib.pyplot as plt

# Sample Data
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Plotting the scatter graph comparing Mathematics and Science marks
plt.scatter(math_marks, science_marks, color='blue',
            alpha=0.7, edgecolor='black')

# Adding labels and title
plt.title('Scatter Plot: Mathematics vs Science Marks')
plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')

# Display the plot
# plt.grid(True)
plt.show()
