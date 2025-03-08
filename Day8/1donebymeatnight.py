# Importing Necessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder  # For encoding categorical data
from sklearn.feature_extraction.text import TfidfVectorizer  # TF-IDF Vectorizer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
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

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix, df['label'], test_size=0.2, random_state=42)

# Defining models
models = {
    "Logistic Regression": LogisticRegression(),
    "Naive Bayes": MultinomialNB(),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Support Vector Machine": SVC(kernel='linear'),
    "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=5)
}

# Training and evaluating models
results = {}
reports = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy
    reports[name] = classification_report(y_test, y_pred)

    # Confusion Matrix Plot
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=["Fake", "True"], yticklabels=["Fake", "True"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title(f"Confusion Matrix - {name}")
    plt.savefig(f"{name}_confusion_matrix.png")  # Save instead of show
    plt.close()

# Finding the best model
best_model = max(results, key=results.get)
print(f"Best Performing Model: {best_model} with Accuracy: {results[best_model]:.4f}")

# GUI to Display Results
def show_results():
    root = tk.Tk()
    root.title("Model Evaluation Results")

    frame = ttk.Frame(root, padding=10)
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text="Model Performance", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2)
    
    row_num = 1
    for name, accuracy in results.items():
        ttk.Label(frame, text=f"{name}: {accuracy:.4f}", font=("Arial", 12)).grid(row=row_num, column=0, sticky=tk.W)
        row_num += 1
    
    ttk.Label(frame, text=f"Best Model: {best_model} with Accuracy: {results[best_model]:.4f}", font=("Arial", 12, "bold")).grid(row=row_num, column=0, columnspan=2, pady=10)
    
    root.mainloop()

# Show the GUI
show_results()

# Testing with a sample input
input_text = "This is a fake news article."
input_vector = vectorizer.transform([input_text])
final_prediction = models[best_model].predict(input_vector)
print(f"Best Model Prediction for Input: {final_prediction}")
