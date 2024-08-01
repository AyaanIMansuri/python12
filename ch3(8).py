# Declare two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Perform union operation
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Perform intersection operation
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Perform difference operation (elements in set1 but not in set2)
difference_set = set1.difference(set2)
print("Difference of set1 and set2 (set1 - set2):", difference_set)

# Perform symmetric difference operation
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference_set)
