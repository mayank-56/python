import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cur = con.cursor()

# List containing column information (name, datatype, size)
columns = [
    ("name", "varchar", 20),
    ("qualification", "varchar", 20),
    ("post", "varchar", 20),
    ("salary", "int", 6)
]

# Create column definition string
col_def = ""

for col in columns:
    if col[1] == "varchar":
        col_def += f"{col[0]} {col[1]}({col[2]}), "
    else:
        col_def += f"{col[0]} {col[1]}({col[2]}), "

# Remove last comma
col_def = col_def.rstrip(", ")

# Create table query
query = f"CREATE TABLE employee ({col_def})"

# Execute query
cur.execute(query)

print("Table created successfully")

con.close()
