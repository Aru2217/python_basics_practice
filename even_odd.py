""" question check even or odd
   user enters a number.
   if divisible by 2 "even"
   Else "odd" """
Number = int(input("enter your number : "))
if Number % 2 == 0 :# % gives remainder, even numbes gives remainder 0
    print("Its Even Number")
else:
    print("Its Odd Number")