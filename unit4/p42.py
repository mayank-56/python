import pandas as pd
import re

# Load Excel file
df = pd.read_excel("students.xlsx")

# Regular expression for valid email
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

print("Students with Valid Emails:\n")

# Check each email
for index, row in df.iterrows():
    email = str(row['E-Mail'])
    
    if re.match(pattern, email):
        print(row)
        print()
