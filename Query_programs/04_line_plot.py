import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Date': ['01-04-2020', '02-04-2020', '03-04-2020', '06-04-2020', '07-04-2020', '08-04-2020', '09-04-2020', '13-04-2020', '14-04-2020', '15-04-2020', '16-04-2020'],
    'Open': [1098.26, 1119.015, 1097.97, 1138, 1221, 1206.5, 1224.08, 1209.18, 1245.09, 1245.61, 1274.1],
    'High': [1126.86, 1123.54, 1067.34, 1194.66, 1225, 1219.07, 1225.57, 1220.51, 1282.07, 1280.46, 1279],
    'Low': [1096.4, 1079.81, 1089.34, 1130.94, 1182.23, 1188.16, 1196.735, 1187.598, 1236.93, 1240.4, 1242.62],
    'Close': [1105.62, 1120.84, 1097.88, 1186.92, 1186.51, 1210.28, 1211.45, 1217.56, 1269.23, 1262.47, 1263.47],
    'Adj Close': [1120.84, 1097.88, 1045.56, 1186.92, 1186.51, 1210.28, 1211.45, 1217.56, 1269.23, 1263.47, 1263.47],
    'Volume': [2343100, 1964900, 2313400, 2664700, 2387300, 1975100, 2175400, 1739800, 2470400, 1671700, 1245.67]
}

# Create a DataFrame
stock_df = pd.DataFrame(data)

# Convert 'Date' column to datetime type
stock_df['Date'] = pd.to_datetime(stock_df['Date'], format='%d-%m-%Y')

# Filter data between two specific dates
start_date = '2020-04-01'
end_date = '2020-04-15'
filtered_stock_df = stock_df[(stock_df['Date'] >= start_date) & (stock_df['Date'] <= end_date)]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(filtered_stock_df['Date'], filtered_stock_df['Close'], marker='o', linestyle='-', color='b')
plt.title('Alphabet Inc. Stock Prices between {} and {}'.format(start_date, end_date))
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.show()
