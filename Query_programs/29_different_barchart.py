import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ['blue', 'green', 'red', 'yellow',
          'orange', 'purple']  # Different colors for bars

# Creating a bar chart with different colors for each bar
plt.figure(figsize=(8, 6))
plt.bar(languages, popularity, color=colors)

# Adding labels and title
plt.xlabel('Programming Languages')
plt.ylabel('Popularity')
plt.title('Popularity of Programming Languages')

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Displaying the plot
plt.tight_layout()
plt.show()
