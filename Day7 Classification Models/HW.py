import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("Day4/crop.csv")


#Data cleaning

#Checking for null values
# print(df.isnull().any().any())
# print(df.isna())

#filling null values with 0
df.fillna(0)


#Summer Season

print(df[df['season'] == 'summer'].describe())

summer_season = df[df['temperature'].between(24, 32)& 
                  df['humidity'].between(17, 94)& 
                  df['ph'].between(3.5,10)& 
                  df['water availability'].between(20, 74.5)]

#Winter Season

print(df[df['season'] == 'winter'].describe())

winter_season = df[df['temperature'].between(17, 24) & 
                   df['humidity'].between(14, 85) & 
                   df['ph'].between(5.5, 9) & 
                   df['water availability'].between(60, 75)]


#Rainy Season

print(df[df['season'] == 'rainy'].describe())

rainy_season = df[df['temperature'].between(23, 36) & 
                   df['humidity'].between(30, 90) & 
                   df['ph'].between(4.5, 8) & 
                   df['water availability'].between(35, 299)]

#Spring Season

print(df[df['season'] == 'spring'].describe())

spring_season = df[df['temperature'].between(15, 25) & 
                   df['humidity'].between(18, 25) & 
                   df['ph'].between(5.5, 6) & 
                   df['water availability'].between(60, 150)]


#Drop The Season Column
df.drop('season', axis=1, inplace=True)

#data visualization

pir_data= np.array([len(summer_season),len(winter_season),len(rainy_season),len(spring_season)])

labels = ['summer', 'winter', 'rainy', 'spring']

plt.pie(pir_data, labels=labels, autopct='%1.1f%%')
plt.show()


#Creating dependented variable and independent variable

y = df['label']
x = df.iloc[:,0:4]
print("Dependent variable: ")
print(y)
print("Independent variable: ")
print(x)


#Splitting the data into training and testing sets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Training the Gaussian Naïve Bayes model
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Making a prediction
input_data = (24, 85, 5.5, 60)
input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)

prediction = gnb.predict(input_data_as_numpy_array)
print(prediction)

# Evaluate the model
y_pred = gnb.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Classification Report: \n", classification_report(y_test, y_pred))

