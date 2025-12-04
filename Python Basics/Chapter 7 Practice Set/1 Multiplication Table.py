number = int(input("\nEnter a number to generate its multiplication table: "))

print(f"\nMultiplication Table for {number}:")

print("\n-------------------------")

for i in range(1, 11):
    print(f"{number} X {i} = {number * i}")
