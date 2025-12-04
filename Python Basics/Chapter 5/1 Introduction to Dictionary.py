print("\n\nIntroduction to Dictionary in Python")
print("-----------------------------------\n")
print("A dictionary in Python is an unordered collection of items. Each item is a key-value pair.\nDictionary is Mutable, meaning you can change its content without changing its identity.\n")
print("syntax: my_dict = {key1: value1, key2: value2, ...}\n\n")


marks={
    "Viraj": 85,
    "Prathamesh": 92,
    "Rohan": 78,
    "Shubham": 88
}

print(type(marks))  # Checking the type of the dictionary
print(marks["Prathamesh"])  # Accessing value using key
