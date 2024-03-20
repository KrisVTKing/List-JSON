import json

filename = 'Names.json'

name = input("Enter your name: ")

# Initialize people as an empty list
people = []

try:
    # Try to open the JSON file and load its contents
    with open(filename) as f:
        # Load the data from the file into the people list
        data = json.load(f)
        # Check if data is a dictionary with a "people" key
        if isinstance(data, dict) and "people" in data:
            people = data["people"]
except FileNotFoundError:
    # If the file doesn't exist, just pass (do nothing)
    pass

# Check if the name is already in the list
if any(person["name"] == name for person in people):
    add_name = input("The name is already in the list. Do you want to add it again? (yes/no): ").lower()
    if add_name != 'yes':
        # If the user doesn't want to add the name, exit the program
        print("Exiting program.")
        exit()
else:
    add_name = input("The name is not in the list. Do you want to add it? (yes/no): ").lower()
    if add_name != 'yes':
        # If the user doesn't want to add the name, exit the program
        print("Exiting program.")
        exit()

# Append the new person to the people list
people.append({"name": name})

# Write the updated people list back to the JSON file
with open(filename, 'w') as f:
    json.dump({"people": people}, f, indent=4)

print("Name added successfully.")