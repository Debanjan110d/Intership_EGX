import pandas as pd

df = pd.read_csv("Day4/crop.csv")
print(df)
# print(df.columns)
# print(df[df['season'] == 'rainy'])

# print("UNIQUE VALUES based on the season ")
# unique_crops_by_season = df.groupby('season')['label'].unique()
# print(unique_crops_by_season)

