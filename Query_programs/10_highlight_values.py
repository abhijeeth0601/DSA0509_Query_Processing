import pandas as pd
import numpy as np
import imgkit

# Generating random data for the DataFrame
data = {
    'A': list(range(1, 11)),
    'B': np.random.randn(10),     # Random values for column B
    'C': np.random.randn(10),     # Random values for column C
    'D': np.random.randn(10),     # Random values for column D
    'E': np.random.randn(10)      # Random values for column E
}

# Creating the DataFrame
df = pd.DataFrame(data)


def negative_highlighter(x):
    is_negative = x < 0
    return ["color: #EE2E31" if i else "color: #000000" for i in is_negative]


# Apply color formatting to the DataFrame
styled_df = df.style.apply(negative_highlighter)

# Save the styled DataFrame as an image
html_file = 'styled_dataframe.html'
styled_df.to_html(html_file)

styled_df.to_excel("highlight.xlsx")
