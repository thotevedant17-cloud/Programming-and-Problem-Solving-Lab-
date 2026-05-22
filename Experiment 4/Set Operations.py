# Taking input for Set A
set_a = set(map(int, input("Set A: ").split()))

# Taking input for Set B
set_b = set(map(int, input("Set B: ").split()))

# Performing operations
union_set = set_a.union(set_b)
intersection_set = set_a.intersection(set_b)
difference_set = set_a.difference(set_b)

# Printing results
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)

