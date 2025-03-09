# Importing Necessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import tkinter as tk
from tkinter import ttk

# Reading Dataset
fake_news = pd.read_csv("Day8/Fake.csv")
true_news = pd.read_csv("Day8/True.csv")

# Assigning labels: Fake = 0, True = 1
fake_news['label'] = 0
true_news['label'] = 1

# Concatenating the data
df = pd.concat([fake_news, true_news], axis=0)

# Lowercasing all text data
df['title'] = df['title'].str.lower()
df['text'] = df['text'].str.lower()

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
df[['subject']] = encoder.fit_transform(df[['subject']])

# Applying TF-IDF Vectorizer to 'text' and 'title'
vectorizer_text = TfidfVectorizer(stop_words='english', max_features=5000)
vectorizer_title = TfidfVectorizer(stop_words='english', max_features=1000)

tfidf_text = vectorizer_text.fit_transform(df['text'])
tfidf_title = vectorizer_title.fit_transform(df['title'])

# Combining both feature sets
from scipy.sparse import hstack
X = hstack([tfidf_text, tfidf_title])
y = df['label']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Defining models
models = {
    "Logistic Regression": LogisticRegression(),
    "Naive Bayes": MultinomialNB(),
    "Random Forest": RandomForestClassifier(),
    "SVM": SVC(),
    "KNN": KNeighborsClassifier()
}

# Training and evaluating models
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy
    print(f"{name} Accuracy: {accuracy:.4f}")
    print(classification_report(y_test, y_pred))

# GUI to display results
def show_results():
    root = tk.Tk()
    root.title("Model Performance")
    
    frame = ttk.Frame(root, padding=10)
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    ttk.Label(frame, text="Model Performance", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
    
    row_num = 1
    for model, score in results.items():
        ttk.Label(frame, text=model, font=("Arial", 12)).grid(row=row_num, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Label(frame, text=f"{score:.4f}", font=("Arial", 12)).grid(row=row_num, column=1, padx=10, pady=5, sticky=tk.W)
        row_num += 1
    
    root.mainloop()

# Show results in GUI
show_results()
