import json

# Create a JSON file to store user credentials
users_data = {
    "users": []
}

# Write the initial data to a JSON file
with open('login.json', 'w') as file:
    json.dump(users_data, file, indent=4)

print("JSON file for storing user credentials created successfully!")