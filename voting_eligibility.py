"""question voting eligiblity
   check if a person is eligible to vote
   user enters age.
   if age is 18 or more,print "eligible"
   otherwise print" not eligible" """
age = int(input('Enter your age : '))
if age>=18 :
    print("you are eligible for voting")
else:
    print("you ae not eligible for voting")
