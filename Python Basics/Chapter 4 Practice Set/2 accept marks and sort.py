# Printing marks of 5 Students entered by user in a sorted manner

marks= [ ]

marks1 = int(input("Enter marks for subject 1: "))
marks.append(marks1)

marks2 = int(input("Enter marks for subject 2: "))
marks.append(marks2)

marks3 = int(input("Enter marks for subject 3: "))
marks.append(marks3)

marks4 = int(input("Enter marks for subject 4: "))
marks.append(marks4)

marks5 = int(input("Enter marks for subject 5: "))
marks.append(marks5)


print("\n\nThe marks you entered are: ", marks)

marks.sort()
print("\n\nThe sorted marks are: ", marks)
