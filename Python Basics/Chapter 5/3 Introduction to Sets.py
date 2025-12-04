set1 = {1, 5, 67, 22, 45, 34, 82}

print("Hello, welcome to the world of Sets in Python!")
print("----------------------------------------------\n")
print("A set in Python is an unordered collection of unique items. \nSets are mutable, meaning you can add or remove items after its creation.\n")

print("syntax: my_set = {item1, item2, item3, ...}\n\n")
print("Type of set1 is : ", type(set1))
print("Set 1:", set1)

set2 = {"Apple", "Banana", "Cherry"}
print("Set 2:", set2)

set1.add(100)  # Adding an element to set1
print("Set 1 after adding 100:", set1)

set2.remove("Banana")  # Removing an element from set2
print("Set 2 after removing 'Banana':", set2)
