import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Creating a horizontal bar chart
plt.figure(figsize=(8, 6))
# Use plt.barh for horizontal bar chart
plt.barh(languages, popularity, color='skyblue')

# Adding labels and title
plt.xlabel('Popularity')
plt.ylabel('Programming Languages')
plt.title('Popularity of Programming Languages')

# Displaying the plot
plt.tight_layout()
plt.show()
