# Author :- Biresashis Das

# To check whether a number is odd or even.

number = int(input("Which number do you want to check? "))

#If remainder zero after divided by 2, number is even
if number % 2 == 0:
    print("This is an even number")
#If remainder not zero after divided by 2, number is even
else:
    print("This is an odd number")
