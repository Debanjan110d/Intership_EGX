import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# Load the CSV file into a DataFrame
df = pd.read_csv("Day4/crop.csv")

# Print the entire DataFrame
print(df)

# Print the column names of the DataFrame
print(df.columns)



# Group the DataFrame by 'season' and count unique values in the 'label' column
print("UNIQUE VALUES based on the season ")
unique_crops_by_season = df.groupby('season')['label'].nunique()

# Create a pie chart for the number of unique crops per season
plt.pie(unique_crops_by_season, labels=unique_crops_by_season.index, autopct='%1.1f%%')

# Set the title of the pie chart
plt.title("Number of crops per season")

# Display the pie chart we have to use show()
plt.show()

# Bar chart for the number of each crop
crop_counts = df['label'].value_counts()
plt.pie(crop_counts.values, labels=crop_counts.index, autopct='%1.1f%%')
plt.title('Number of each crop')
plt.show()
