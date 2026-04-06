import pandas as pd

# Load Excel file
df = pd.read_excel("students.xlsx")

# Display column names
print("Columns in Excel File:")
print(df.columns)

print("\nData Types of Each Column:")
print(df.dtypes)
