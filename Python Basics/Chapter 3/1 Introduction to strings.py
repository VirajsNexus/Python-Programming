a = 'Viraj'                                         # Single quotes
b = "I love Programming"                            # Double quotes
c = '''Welcome to Chapter 3 : String in python'''   # Triple quotes

print(a)
print(b)
print(c)

print("String is immutable\n" 
" means once it is created, its elements cannot be changed or replaced.\n" \
" You can create a new string based on the existing string.\n"\
" For example:\n" \
" If we try to change the first character of the string a from 'V' to 'v', it will result in an error.\n" \
)

# SLicing in Python 

# variable_name = string_to_be_sliced[start_index : end_index]
name = "Viraj Jamdhade"
slice = name[0:5]  # Slicing the string from index 0 to 4

print("Sliced string :", slice)

#Negative Slicing
neg_slice = name[-8:-1]  # Slicing the string from index -7 to -2
print("Negative Sliced string:", neg_slice)


# slicing with skip value
skip_slice = name[0:13:3]  # Slicing the string from index 0 to 12 with a skip value of 2
print("Sliced string with skip value:", skip_slice)
