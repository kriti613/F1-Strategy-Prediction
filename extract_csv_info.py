import pandas as pd

# Read CSV
df = pd.read_csv('F1-Dataset/status.csv')  # Replace with your CSV file name

# Show basic info
print("First 5 rows:\n", df.head())
print("\nColumn names:\n", df.columns.tolist())
print("\nShape of the file (rows, columns):\n", df.shape)
print("\nData types of each column:\n", df.dtypes)

# Example: Extract a specific column
print("\nExtracted Column 'Name':\n", df['Name'])  # replace 'Name' with your column

# Example: Basic summary
print("\nSummary Statistics:\n", df.describe())
