
print("Tuples in Python")
print("Tuples are immutable, meaning once created, their content cannot be changed.\n")


tuple1 = (1, 2, 3, 4, 5)

print("Original Tuple: ", tuple1)
print("Type of tuple1: ", type(tuple1))
print("Element at index 2: ", tuple1[2])  # Accessing element at index 2
print("Slicing tuple from index 1 to 4: ", tuple1[1:4])  # Slicing from index 1 to 3
print("Length of tuple1: ", len(tuple1))  # Length of the tuple
print("Iterating through tuple1:")
for item in tuple1:
    print(item)