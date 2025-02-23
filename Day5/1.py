import pandas as pd

data = {
    
    "Height":[162,170,165,180,175],
    "Weight":[50,60,55,70,65]
    }
df = pd.DataFrame(data)
print(df)

# Calculate the correlation matrix of the DataFrame 'df' and print it
correlation_matrix = df.corr()
print(correlation_matrix)

