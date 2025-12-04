letter  = '''
            Dear <|NAME|>,
            You are selected!
            Date: <|DATE|>'''

print(letter.replace("<|NAME|>", input("Enter your name: ")).replace("<|DATE|>", input("Enter date(DD/MM/YYYY): ")))