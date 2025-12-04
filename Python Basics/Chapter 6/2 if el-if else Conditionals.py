age = int(input("Enter your age: "))

# If elif else ladder
if(age>=18):
    print("\n\nYou are above the age of consent.....")                #This will execute if age is 18 or above    
    print("Good for you!!!!!!!!")

elif(age<0):
    print("\n\nAge annot be negative......")                          #This will execute if age is negative

elif(age==0):
    print("\n\nYou are entering 0 which is not a valid age!!!!!!!")   #This will execute if age is exactly 0

else:
    print("\n\nYou are below the age of consent_______")              #This will execute if none of the above conditions are met


print("\n\n...........End of Program..........")                      #This will always execute