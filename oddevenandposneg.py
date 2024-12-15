# 4. Write a program to find whether the given number is odd or even and positive or negative.

n= int(input("Enter a Number = "))

if(n%2 == 0 ):
    print("Even Number")
else:
    print("Odd Number")

if(n>0):
    print("Positive")
else:
    print("Negative")