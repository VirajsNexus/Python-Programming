marks = int(input("\nEnter your marks: "))

if(marks<=100 and marks>=90):
    grade = "O"
elif(marks<90 and marks>=80):
    grade = "A+"
elif(marks<80 and marks>=70):
    grade = "A"
elif(marks<70 and marks>=60):
    grade = "B"
elif(marks<60 and marks>=50):
    grade = "C"
elif(marks<50):
    grade = "F"

print("\nYour grade is:", grade)