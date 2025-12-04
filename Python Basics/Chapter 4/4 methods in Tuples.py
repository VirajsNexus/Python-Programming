tuple1 = (1, 2, 3, 4, 5,  "Viraj", 7.8, True)
print("Original Tuple: ", tuple1)

print("\n methods in tuple : \n count(element) , index(element) , len(tuple) , slicing(tuple[start_index : end_index]) \n")

# method1 : count() - Returns the number of occurrences of a specified element in the tuple
count_viraj = tuple1.count("Viraj")
print("Count of 'Viraj' in tuple: ", count_viraj)
# method2 : index() - Returns the index of the first occurrence of a specified element in the tuple
index_3 = tuple1.index(3)
print("Index of element '3' in tuple: ", index_3)
# method3 : len() - Returns the number of elements in the tuple
length_of_tuple = len(tuple1)
print("Length of the tuple: ", length_of_tuple)
# method4 : slicing - Accessing a range of elements in the tuple
sliced_tuple = tuple1[2:6]
print("Sliced tuple from index 2 to 5: ", sliced_tuple)
print("\n\nNote: Tuples are immutable, so methods that modify the tuple (like append, remove, etc.) are not available.\n\n")

