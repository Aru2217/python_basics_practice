"""Question on check username length
   Take a username as input.
   if length is lessthan 5, print"Too short".
   Else print "Valid username". """
username = input("enter your username : " )
if len(username) < 5 :
 print("too short")
else :
 print("valid username")