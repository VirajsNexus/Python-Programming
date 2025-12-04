username = input("\nEnter username: ")

lenght_of_username = len(username)      #returns length of string
if(lenght_of_username < 10):
    print("\nYour username contains less than 10 characters")
else:
    print("\nYour username contains more than or equal to 10 characters")