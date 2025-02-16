import pandas as pd

df = pd.read_csv("Day3/Salary_dataset.csv")
salary = pd.read_csv("Day3/Salary_dataset.csv")
print(salary)
# show first few rows of dataframe
print(df.head())
# show last few rows of dataframe
print(df.tail())
# show info of dataframe
print(df.info())
# show summary statistics of dataframe
print(df.describe())
# show columns of dataframe
print(df.columns)
# show index of dataframe
print(df.index)
# show values of dataframe
print(df.values)
#isnull
# checks for null values in dataframe
print(df.isnull())
#notnull
# checks for not null values in dataframe
print(df.notnull())
# drops rows with any null values
#fillna
# fills null values with 0
print(df.fillna(0))
#drop duplicates
print(df.drop_duplicates())
#sort values
print(df.sort_values("YearsExperience"))
#sort values ulto kore
print(df.sort_values("YearsExperience",ascending=False))
#groupby
print(df.groupby("YearsExperience").mean()) # calculate mean of all columns for each group
print(df.groupby("YearsExperience").median()) # calculate median of all columns for each group
print(df.groupby("YearsExperience").sum()) # calculate sum of all columns for each group
print(df.groupby("YearsExperience").count()) # calculate count of all columns for each group
print(df.groupby("YearsExperience").std()) # calculate standard deviation of all columns for each group
print(df.groupby("YearsExperience").min()) # calculate minimum of all columns for each group
print(df.groupby("YearsExperience").max()) # calculate maximum of all columns for each group
print(df.groupby("YearsExperience").var()) # calculate variance of all columns for each group
#sum
print(df.isnull().sum())
#dropna
print(df.dropna())#it createas a new virtual dataframe
#to prevent it from creating a new virtual dataframe and making changes to the original dataframe
# df.dropna(inplace=True) 
#drop duplicates
print(df.drop_duplicates())
#drop
print(df.drop("YearsExperience",axis=1))
