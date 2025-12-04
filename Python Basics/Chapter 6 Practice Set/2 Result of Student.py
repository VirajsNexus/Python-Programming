marks1 = int(input("Enter Marks of subject 1: "))
marks2 = int(input("Enter Marks of subject 2: "))
marks3 = int(input("Enter Marks of subject 3: "))

# Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("\nYou are passed:", total_percentage)

else:
    print("\nYou failed, try again next year:", total_percentage)