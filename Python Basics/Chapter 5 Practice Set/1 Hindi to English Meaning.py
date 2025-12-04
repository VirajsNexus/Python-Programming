Words = {
    "Madat": "Help",
    "Pustak": "Book",
    "Vidyalaya": "School",
    "Shikshak": "Teacher",
    "Chhatra": "Student",
    "Dosti": "Friendship",
}

print("Welcome to Hindi to English Meaning Finder")
print("The available words are: ", list(Words.keys()))
word = input("Enter the word you want meaning of : ")

print("The meaning of ' ", word, " ' is:", Words.get(word, "Word not found in the dictionary"))
