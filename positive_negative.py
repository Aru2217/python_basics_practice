""" Question Check if a number is positive,negative,or zero.
    user enters a number .
    output should be :
    "positive"if number > 0
    "Negative"if number <0
    "zero"if number == 0. """
Number = int(input("Enter your number : "))
if Number > 0 :
    print("Positive")
elif Number < 0 :
    print("Negative")
elif Number == 0 :
    print("Zero")