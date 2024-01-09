import pandas as pd
import numpy as np

# Generating random data for the DataFrame
data = np.random.randn(10, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Function to set background color and font color


def style_background_yellow(val):
    return f'background-color: black; color: yellow'


# Apply the styling to the entire DataFrame
styled_df = df.style.map(style_background_yellow)

# Display the styled DataFrame
styled_df.to_excel("Background_color.xlsx")
