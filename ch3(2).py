# Initialize a list
my_list = [1, 2, 3, 4, 5]

# Function to insert an element at a specific position
def insert_element(lst, element, position):
    lst.insert(position, element)
    print(f"After inserting {element} at position {position}: {lst}")

# Function to update an element at a specific position
def update_element(lst, position, new_value):
    if position < len(lst):
        old_value = lst[position]
        lst[position] = new_value
        print(f"After updating position {position} from {old_value} to {new_value}: {lst}")
    else:
        print(f"Position {position} is out of range.")

# Function to delete an element at a specific position
def delete_element(lst, position):
    if position < len(lst):
        removed_value = lst.pop(position)
        print(f"After deleting element at position {position} (value {removed_value}): {lst}")
    else:
        print(f"Position {position} is out of range.")

# Function to search for an element in the list
def search_element(lst, element):
    if element in lst:
        position = lst.index(element)
        print(f"Element {element} found at position {position}.")
    else:
        print(f"Element {element} not found in the list.")

# Display the initial list
print("Initial list:", my_list)

# Insert an element
insert_element(my_list, 6, 2)

# Update an element
update_element(my_list, 3, 10)

# Delete an element
delete_element(my_list, 4)

# Search for an element
search_element(my_list, 10)

# Search for an element that is not in the list
search_element(my_list, 99)
