import pandas as pd

# Creating the DataFrame
data = {
    'Text_Column': ['apple', 'Banana', 'oRange', 'grape', 'KiWi']
}

df = pd.DataFrame(data)

# Swapping the cases of a specified character column
column_name = 'Text_Column'
df[column_name] = df[column_name].str.swapcase()

# Displaying the updated DataFrame
print("DataFrame after swapping cases:")
print(df)
