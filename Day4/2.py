import pandas as pd

data ={
    "Name":["John","Anna","John","Max","Anna","Eva"],
    "Age":[28,24,28,35,24,38],
    "Country":["USA","UK","USA","Germany","UK","Sweden"],
    "Salary":[5000,6000,5000,7000,6000,8000]
    }
df = pd.DataFrame(data)
print(df)
print ("\n")
df.drop_duplicates(subset=["Name"], keep="first", inplace=True)
print(df)

#New colum and values
df["Salary_INR"] = df["Salary"] * 84
print(df)

#Work on previous column
df["Salary"] = df["Salary"].apply(lambda x: x * 84)
print(df)

