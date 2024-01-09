import pandas as pd

# Creating the DataFrame
data = {
    'Text_Column': ['apple', 'banana', 'orange', 'grape', 'kiwi']
}

df = pd.DataFrame(data)

# Finding the index of a given substring within a column
substring = 'ran'
column_name = 'Text_Column'

indices = df[df[column_name].str.contains(substring)].index
print(f"The indices where '{substring}' is present in '{column_name}' column:")
print(indices)
