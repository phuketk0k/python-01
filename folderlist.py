import os

folders = input("Please enter folder list: ")



for folder in folders: 
    try:
    
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name")
        continue

    except PermissionError:
        print("Tu eres no sudo!")
        continue

   
    for file in files:
        print(file)


