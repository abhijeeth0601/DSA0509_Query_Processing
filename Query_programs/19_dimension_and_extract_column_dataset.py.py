import pandas as pd

# Creating the DataFrame
data = {
    'Year': [1986, 1986, 1985, 1986, 1987],
    'Who Region': ['Western Pacific', 'Americas', 'Africa', 'Americas', 'Americas'],
    'Country': ['Viet Nam', 'Uruguat', "Cte d'Ivoire", 'Colombia', 'Saint Kitta and Nevis'],
    'Beverage Type': ['Wine', 'Other', 'Wine', 'Beer', 'Beer'],
    'Display Value': [0, 0.5, 1.62, 4.27, 1.98]
}

df = pd.DataFrame(data)

# Displaying the dimensions (shape) of the DataFrame
print("Dimensions of the DataFrame (rows, columns):", df.shape)

# Displaying the column names of the DataFrame
print("\nColumn names:")
print(df.columns)
