import pandas as pd
import numpy as np

# Creating the DataFrame
data = {
    'A': list(range(1, 11)),
    'B': [1.329210, -1.070820, -1.626400, 0.961538, 1.453420, -1.336940, -1.325960, 0.354493, 1.627800, -0.129820],
    'C': [-0.770033, -1.438710, 0.219565, 0.104011, 1.057740, 0.562861, np.nan, 1.037530, 8.000000, 0.631523],
    'D': [-0.316280, 0.564417, np.nan, -0.481165, 0.165562, 1.392850, 0.519818, 1.207600, 9.000000, -0.586538],
    'E': [-0.990810, 0.295722, 1.889270, 0.850229, 0.515018, np.nan, 1.428980, -0.002040, np.nan, 0.290720]
}

# Creating the DataFrame with mixed values
df = pd.DataFrame(data)

print(df)

null_values = df.style.highlight_null(color="red")
null_values.to_excel("highlight_NAN.xlsx")
