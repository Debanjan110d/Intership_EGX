Pandas is a powerful Python library used for **data analysis and manipulation**. It provides flexible data structures like **Series** and **DataFrames**, making it easy to handle structured data. Here are all the major uses of pandas:

---

## **1. Data Creation**

-  Creating **Series** (1D array)
   ```python
   import pandas as pd
   s = pd.Series([10, 20, 30, 40])
   print(s)
   ```
-  Creating **DataFrame** (2D table)
   ```python
   data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
   df = pd.DataFrame(data)
   print(df)
   ```

---

## **2. Data Loading & Exporting**

-  **Reading data from files:**
   ```python
   df = pd.read_csv("data.csv")       # CSV file
   df = pd.read_excel("data.xlsx")    # Excel file
   df = pd.read_json("data.json")     # JSON file
   df = pd.read_sql("SELECT * FROM table", conn)  # SQL database
   ```
-  **Saving data to files:**
   ```python
   df.to_csv("output.csv", index=False)
   df.to_excel("output.xlsx", index=False)
   df.to_json("output.json")
   ```

---

## **3. Data Exploration**

-  **Viewing top/bottom rows**
   ```python
   print(df.head())  # First 5 rows
   print(df.tail())  # Last 5 rows
   ```
-  **Checking structure**
   ```python
   print(df.info())   # Data types and non-null values
   print(df.describe())  # Summary statistics (numerical columns)
   print(df.shape)  # (rows, columns)
   ```

---

## **4. Selecting & Filtering Data**

-  **Selecting specific columns**
   ```python
   print(df['Name'])  # Single column
   print(df[['Name', 'Age']])  # Multiple columns
   ```
-  **Filtering rows based on condition**
   ```python
   df_filtered = df[df['Age'] > 25]
   ```
-  **Using multiple conditions**
   ```python
   df_filtered = df[(df['Age'] > 25) & (df['Name'] == 'Alice')]
   ```
-  **Selecting rows by index**
   ```python
   print(df.iloc[0])  # First row
   print(df.loc[0, 'Name'])  # First row, 'Name' column
   ```

---

## **5. Data Cleaning**

-  **Handling missing values**
   ```python
   df.dropna()  # Remove rows with NaN
   df.fillna(0)  # Replace NaN with 0
   ```
-  **Replacing values**
   ```python
   df.replace({'old_value': 'new_value'}, inplace=True)
   ```
-  **Renaming columns**
   ```python
   df.rename(columns={'OldName': 'NewName'}, inplace=True)
   ```

---

## **6. Data Transformation**

-  **Adding a new column**
   ```python
   df['Salary'] = df['Age'] * 1000
   ```
-  **Applying functions**
   ```python
   df['Age'] = df['Age'].apply(lambda x: x + 1)  # Increase age by 1
   ```
-  **Changing data type**
   ```python
   df['Age'] = df['Age'].astype(float)
   ```

---

## **7. Grouping & Aggregation**

-  **Grouping data**
   ```python
   df.groupby('Category').mean()
   ```
-  **Aggregating data**
   ```python
   df.groupby('Category').agg({'Sales': 'sum', 'Profit': 'mean'})
   ```
-  **Pivot Tables**
   ```python
   df.pivot_table(values='Sales', index='Region', columns='Year', aggfunc='sum')
   ```

---

## **8. Sorting & Ranking**

-  **Sorting data**
   ```python
   df.sort_values(by='Age', ascending=False)
   ```
-  **Ranking values**
   ```python
   df['Rank'] = df['Salary'].rank()
   ```

---

## **9. Merging, Joining & Concatenation**

-  **Merging two DataFrames**
   ```python
   df_merged = pd.merge(df1, df2, on='ID')
   ```
-  **Joining based on index**
   ```python
   df_joined = df1.join(df2, lsuffix='_left', rsuffix='_right')
   ```
-  **Concatenation**
   ```python
   df_combined = pd.concat([df1, df2], axis=0)  # Stack rows
   ```

---

## **10. Time Series Analysis**

-  **Converting column to DateTime**
   ```python
   df['Date'] = pd.to_datetime(df['Date'])
   ```
-  **Resampling data**
   ```python
   df.resample('M').sum()  # Monthly aggregation
   ```
-  **Extracting date parts**
   ```python
   df['Year'] = df['Date'].dt.year
   df['Month'] = df['Date'].dt.month
   ```

---

## **11. Window Functions**

-  **Rolling average**
   ```python
   df['RollingAvg'] = df['Sales'].rolling(window=3).mean()
   ```
-  **Cumulative sum**
   ```python
   df['CumulativeSum'] = df['Sales'].cumsum()
   ```

---

## **12. Handling Duplicate Data**

-  **Finding duplicates**
   ```python
   df.duplicated()
   ```
-  **Removing duplicates**
   ```python
   df.drop_duplicates(inplace=True)
   ```

---

## **13. Data Visualization (with Matplotlib & Seaborn)**

-  **Basic plotting**
   ```python
   df['Sales'].plot(kind='line')
   ```
-  **Histogram**
   ```python
   df['Age'].hist()
   ```
-  **Seaborn bar plot**
   ```python
   import seaborn as sns
   sns.barplot(x='Category', y='Sales', data=df)
   ```

---

## **14. Advanced Operations**

-  **Converting DataFrame to Dictionary**
   ```python
   df.to_dict()
   ```
-  **Converting DataFrame to NumPy array**
   ```python
   df.to_numpy()
   ```
-  **Applying a function to the entire DataFrame**
   ```python
   df.applymap(lambda x: str(x).upper())
   ```

---

## **15. Using Pandas with SQL**

-  **Reading from SQL**
   ```python
   import sqlite3
   conn = sqlite3.connect('database.db')
   df = pd.read_sql_query("SELECT * FROM table_name", conn)
   ```
-  **Writing to SQL**
   ```python
   df.to_sql('new_table', conn, if_exists='replace', index=False)
   ```

---

### 🚀 **Conclusion**

Pandas is an **essential** library for data analysis and manipulation in Python. It can handle everything from **data cleaning, transformation, aggregation, and visualization** to **time series and SQL integration**.
