"""
Question 
name format check
take a name as input 
if first letter is uppercae
and name length is more than 3
print "good name"
else print"invalid name"
"""
Name = input("Enter your name : ")
if Name[0].isupper() and len(Name)>3 :
    print("Good Name")
else:
    print("Invallid Name")