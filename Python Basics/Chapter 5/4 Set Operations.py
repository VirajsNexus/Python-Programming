set1 = {1, 5, 67, 22, 45, 34, 82, 5, 1, 22}
set2 = {22, 34, 90, 100, 5, 200}

print("Set 1:", set1)
print("Set 2:", set2)

set_intersection = set1.intersection(set2)  # Intersection of set1 and set2
print("Intersection of Set 1 and Set 2:", set_intersection)

set_union = set1.union(set2)  # Union of set1 and set2  
print("Union of Set 1 and Set 2:", set_union)

sub_set = {5, 22}
is_subset = sub_set.issubset(set1)  # Check if sub_set is a subset of set1

print(f"Is {sub_set} a subset of Set 1? {is_subset}")

is_superset = set1.issuperset(sub_set)  # Check if set1 is a superset of sub_set
print(f"Is Set 1 a superset of {sub_set}? {is_superset}")
