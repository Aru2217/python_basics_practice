"""
Question check lowercase or not
take a word as a input
if word is all lowercase
print"Lowercase"
else Print"not lowercase"
"""
words = input("Enter your word : ")
if words.islower():
    print("Lowercase")
else:
    print("Not lowercase")