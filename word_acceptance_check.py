"""
Question(Thinking booster)
Take a word as input.
if the word:
is lowercase or its length is grater than 10
print"Accepted"
else"Rejected"
"""
Word = input("Enter your word : ")
if Word.islower() or len(Word)>10 :
    print("Accepted")
else:
    print("Rejected")