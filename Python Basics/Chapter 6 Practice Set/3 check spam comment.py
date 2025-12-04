comment1 = "Make a lot of money"
comment2 = "buy now"  
comment3 = "subscribe this"  
comment4 = "click this"

message = input("\nEnter your comment: ")

if((comment1 in message) or (comment2 in message )or (comment3 in message) or (comment4 in message)):
    print("\nThis comment is a spam")

else:
    print("\nThis comment is not a spam")