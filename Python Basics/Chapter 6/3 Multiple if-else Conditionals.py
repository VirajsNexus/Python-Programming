age = int(input("Enter your age: "))\



# If statement no: 1
if(age%2 == 0):                                         #Checking if a number is even       
    print("\n\nAge entered is even")
# End of If statement no: 1



# If statement no: 2
if(age>=18):
    print("\n\nYou are above the age of consent")           #This will execute if age is 18 or above
    print("Good for you")

elif(age<0):
    print("\n\nYou are entering an invalid negative age")   #This will execute if age is negative

else:
    print("\n\nYou are below the age of consent")           #This will execute if none of the above conditions are met
# End of If statement no: 2

print("\nEnd of Program")