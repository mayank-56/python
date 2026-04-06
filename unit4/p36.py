import pandas as pd

# Load Excel file
df = pd.read_excel("students.xlsx")

print("Original Data:")
print(df)

print("\n---------------------------\n")

# Using dropna() function
print("Data after using dropna() (rows with missing values removed):")
drop_data = df.dropna()
print(drop_data)

print("\n---------------------------\n")

# Using fillna() function
print("Data after using fillna() (missing values replaced):")
fill_data = df.fillna("Not Available")
print(fill_data)
