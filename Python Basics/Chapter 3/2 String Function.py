a = "hello"

print("\n\nOriginal String a: ", a)
print("\nLength of string a is :", len(a))  # Length of string 5

print("Does name ends with 'a'? :", a.endswith('a'))  # False
print("Does name starts with 'h'? :", a.startswith('he'))  # True

print("Capatalized String : ", a.capitalize())  # Hello
print("Uppercase String : ", a.upper())  # HELLO
print("Lowercase String : ", a.lower())  # hello
print("Title Case String : ", a.title())  # Hello
print("Count of 'l' in string a : ", a.count('l'))  # 2
print("Index of 'e' in string a : ", a.index('e'))  # 1
print("Replace 'l' with 'p' in string a : ", a.replace('l', 'p'))  # Heppo
print("Find 'o' in string a : ", a.find('o'))  # 4
print("Find 'z' in string a : ", a.find('z'))  # -1 (not found)
print("String a after spliting : ", a.split('e'))  # ['H',
print("String a after reversing : ", a[::-1])  # olleH

