import zipfile

# Function to zip a file
def zip_file():
    file_name = input("Enter file name to zip: ")
    zip_name = input("Enter zip file name (without .zip): ") + ".zip"
    
    with zipfile.ZipFile(zip_name, 'w') as z:
        z.write(file_name)
    
    print("File zipped successfully!\n")

def unzip_file():
    zip_name = input("Enter zip file name (with .zip): ")
    
    with zipfile.ZipFile(zip_name, 'r') as z:
        z.extractall()
    
    print("File unzipped successfully!\n")

# Menu
while True:
    print("1) Zip File")
    print("2) Unzip File")
    print("3) Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        zip_file()
    elif choice == '2':
        unzip_file()
    elif choice == '3':
        break
    else:
        print("Invalid choice\n")
