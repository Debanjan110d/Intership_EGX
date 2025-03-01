import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 


df = pd.read_csv("Day4/crop.csv")
# print(df)
# print(df['label'].unique())s
# y = df['label']
# print(y)

x= df.iloc[:,1:3]
print(x)

# print(x.corr())