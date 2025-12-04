my_list = [10, 20, 30, "Viraj", 50.5, False]

print("Original List: ", my_list)
# Method 1: append() - Adds an element at the end of the list
my_list.append("Coders")
print("\nAfter append('Coders'): ", my_list)

print("\nmethods in list : \n sorted() , append() , insert(at_index, Element_to_be_insert) , remove() , pop() , clear() , reverse() , sort() \n")
my_list.remove(10)
print("List after ' remove ' operation : ",my_list )

# my_list.sort()
# print("List after ' sort ' operation : ",my_list )   # Note: sort() will raise an error here due to mixed data types

my_list.append("Hello")
print("List after ' append ' operation : ", my_list)

my_list.insert(2, "Python")
print("List after ' insert ' operation : ", my_list)

my_list.pop(3)
print("List after ' pop ' operation : ", my_list)

my_list.reverse()
print("List after ' reverse ' operation : ", my_list)

my_list.clear()
print("List after ' clear ' operation : ", my_list)