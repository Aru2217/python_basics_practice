"""
Question String slicing
 check password last digit
 take a password as a input
 if the last character is a digit
 print "Ends with a digit"
 else print "Does not end with number"
"""
password = input("Enter your password : ")
if password[-1].isdigit():
 print("Ends with digit")
else:
    print("Does not end with number")
