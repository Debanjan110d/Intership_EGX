import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 


df = pd.read_csv("Day4/crop.csv")
X = df.iloc[:,:-1].values
print(X)
y = df.iloc[:,-1].values
print(y)

# Split the dataset into a training set and a test set
# X is the feature set (all columns except the last one)
# y is the target set (the last column)
# test_size=0.2 means that 20% of the dataset will be used for testing and 80% for training
# random_state=42 ensures reproducibility by controlling the randomness of the data split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
