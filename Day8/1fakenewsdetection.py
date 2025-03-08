# Importing Necessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder  # For encoding categorical data
from sklearn.feature_extraction.text import TfidfVectorizer  # TF-IDF Vectorizer
from sklearn.metrics import accuracy_score, classification_report

# Reading Dataset
fake_news = pd.read_csv("Day8/Fake.csv")
true_news = pd.read_csv("Day8/True.csv")

# Assigning labels: Fake = 0, True = 1
fake_news['label'] = 0
true_news['label'] = 1

# Concatenating the data
df = pd.concat([fake_news, true_news], axis=0)

# Checking for null values
print(df.isna().sum())  # Shows count of missing values in each column

# Checking dataset shape
print(df.shape)  # (rows, columns)

# Shuffling the data
df = df.sample(frac=1).reset_index(drop=True)

# Removing unnecessary columns
if 'index' in df.columns and 'date' in df.columns:
    df.drop(['index', 'date'], axis=1, inplace=True)

# Encoding categorical features using OrdinalEncoder
encoder = OrdinalEncoder()
df[['subject']] = encoder.fit_transform(df[['subject']])  # Converts categorical subjects to numerical values

# Applying TF-IDF Vectorizer to text data
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)  # Limiting to top 5000 words
tfidf_matrix = vectorizer.fit_transform(df['text'])  # Converting text into TF-IDF features

# Display the first few rows to verify changes
print(df.head())

# Splitting the data into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix, df['label'], test_size=0.2, random_state=42)

# Training the model
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy Score:", accuracy)

# Print classification report
print("Classification Report:\n", classification_report(y_test, y_pred))

# Print the prediction for the input data
input_text = "This is a fake news article."
input_vector = vectorizer.transform([input_text])
prediction = model.predict(input_vector)
print("Prediction:", prediction)

# Plotting the confusion matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))