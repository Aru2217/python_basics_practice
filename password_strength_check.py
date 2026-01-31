"""
Question Password strength (basic)
take a password as input.
if password is at least 8 And last character is a digit
print"strong password"
else "weak password"
"""
password = input("Enter your password : " )
if password[-1].isdigit()and len(password)>=8 :
 print("strong password")
else:
 print("weak password")