print("There are two types of conditional expressions in Python:\n\t 1. if-else expressions\n\t 2. ternary conditional operator\n")

age = int(input("\nEnter your age: "))
# Using if-else expression
if age >= 18:
    print("\nYou are eligible to vote.\n")
else:
    print("\nYou are not eligible to vote.\n")

# Using ternary conditional operator
# status = "eligible to vote\n" if age >= 18 else "not eligible to vote\n"
# print(f"\nYou are {status}")
