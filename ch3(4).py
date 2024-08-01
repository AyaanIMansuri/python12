# Declare two tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)

# Function to search for an element in a tuple
def search_tuple(t, element):
    if element in t:
        return f"Element {element} found in the tuple."
    else:
        return f"Element {element} not found in the tuple."

# Function to merge two tuples
def merge_tuples(t1, t2):
    return t1 + t2

# Search for an element in tuple1
element_to_search = 3
search_result = search_tuple(tuple1, element_to_search)
print(search_result)

# Merge tuple1 and tuple2
merged_tuple = merge_tuples(tuple1, tuple2)
print("Merged tuple:", merged_tuple)
