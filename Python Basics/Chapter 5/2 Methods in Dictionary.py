marks={
    "Viraj": 85,
    "Prathamesh": 92,
    "Rohan": 78,
    "Shubham": 88
}

print(marks.keys())    # Getting all keys
print(marks.values())  # Getting all values 
print(marks.items())   # Getting all key-value pairs

# Update Dictionary

marks["Rohan"] = 80  # Updating value for key 'Rohan'
print("Updated Dictionary is : ",marks)

print("Length of dictionary 'marks' is : ",len(marks))  # Getting the number of key-value pairs in the dictionary
print("Accessing marks of viraj using '.get' method : ",marks.get("Viraj"))  # Accessing value using get() method
