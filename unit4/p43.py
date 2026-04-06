import pandas as pd
import re

# Load Excel file
df = pd.read_excel("students.xlsx")

# Regular expression for mobile with country code
pattern = r'^\d{2}-\d{10}$'

print("Students with Mobile Number having Country Code:\n")

# Check each record
for index, row in df.iterrows():
    mobile = str(row['Mobile'])
    
    if re.match(pattern, mobile):
        print(row)
        print()
