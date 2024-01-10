import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('fdata.csv')

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y')

# Set 'Date' column as the index
df.set_index('Date', inplace=True)

# Plotting the line charts for Open, High, Low, Close prices
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Open'], label='Open', marker='o')
plt.plot(df.index, df['High'], label='High', marker='o')
plt.plot(df.index, df['Low'], label='Low', marker='o')
plt.plot(df.index, df['Close'], label='Close', marker='o')

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Financial Data of Alphabet Inc. (Oct 3-7, 2016)')
plt.legend()

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Displaying the plot
plt.tight_layout()
plt.show()
