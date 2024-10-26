import json

employee = {
   "name": "Spongebob",
   "age": 30,
   "job": "Cook"
}

file_path = "output.json"

try:
    with open(file_path, 'w') as file:
        json.dump(employee, file, indent=4)
        print(f"JSON file '{file_path}' has been created successfully")
except FileExistsError:
    print("That file already exists!")