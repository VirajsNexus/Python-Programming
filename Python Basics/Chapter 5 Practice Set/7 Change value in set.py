set1 = {8, 7, 123, "Viraj, [1, 2, 3]"}

print("The original set is : ", set1)  # Output: The original set is :  {8, 7, 123, 'Viraj, [1, 2, 3]'}

# set1[4] [0] = 18  # This will raise an error because set elements are immutable

set1.remove(123)  # Removing an element from the set
set1.add(18)      # Adding a new element to the set

print("The modified set is : ", set1)  # Output: The modified set is :  {8, 18, 7, 'Viraj, [1, 2, 3]'}