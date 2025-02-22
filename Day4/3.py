import pandas as pd

data = {
    "Name":["John","Anna","John","Max","Anna","Eva"],
    "Age":[28,24,28,35,24,38],
    "Country":["USA","UK","USA","Germany","UK","Sweden"],
    "Salary":[5000,6000,5000,7000,6000,8000]
    }
df = pd.DataFrame(data)
print(df)
print ("\n")

print("Sum of Salary: ", df['Salary'].sum())
#or
print("Sum of Salary: ", df['Salary'].agg('sum'))

print ("\n")


#sir code
df["remarks"]=df["quantity"].apply(lambda x: "stock full" if x > 50 else "stock needed")
