# Declare a dictionary
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# Function to insert a new key-value pair into the dictionary
def insert_into_dict(d, key, value):
    d[key] = value
    print(f"Inserted ({key}: {value}) into the dictionary.")

# Function to update an existing key-value pair in the dictionary
def update_dict(d, key, value):
    if key in d:
        d[key] = value
        print(f"Updated ({key}: {value}) in the dictionary.")
    else:
        print(f"Key '{key}' not found in the dictionary.")

# Function to delete a key-value pair from the dictionary
def delete_from_dict(d, key):
    if key in d:
        del d[key]
        print(f"Deleted key '{key}' from the dictionary.")
    else:
        print(f"Key '{key}' not found in the dictionary.")

# Function to search for a key in the dictionary
def search_dict(d, key):
    if key in d:
        return f"Found ({key}: {d[key]}) in the dictionary."
    else:
        return f"Key '{key}' not found in the dictionary."

# Insert a new key-value pair
insert_into_dict(my_dict, 'email', 'alice@example.com')

# Update an existing key-value pair
update_dict(my_dict, 'age', 26)

# Delete a key-value pair
delete_from_dict(my_dict, 'city')

# Search for a key in the dictionary
search_result = search_dict(my_dict, 'name')
print(search_result)

# Display the final state of the dictionary
print("The final dictionary is:", my_dict)
