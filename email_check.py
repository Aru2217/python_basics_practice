"""
Question
Email check (basics)
take an email as input 
if email contains @
print"valid email"
else print"invalid email" 
"""
Email = input("Enter your email : ")
if "@" in Email and "."in Email :
    print("valid Email")
else:
    print("Invalid Email")