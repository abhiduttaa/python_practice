# Write logical expressions for the fouorting:

# A. Either A is greater than B or A is less than C.

a=int(input("enter a number="))
b=int(input("enter a number="))
c=int(input("enter a number="))

logic= (a>=b) or (a<=c) 
print(logic)

# B. The favourite city is either Mumbai or chennai
city=input("enter Your Choice Cityname=")
c = (city == "mumbai") or (city == "chennai")
print(c)

# C. Either the place is Bengaluru or chennai and not Hyderabad

place = input("enter a place=")
p= (place == "Bengaluru") or (place == "chennai") and (place != "Hyderabad")
print(p)

# D. Mark is either greater than 60 but not less than 90

m = float(input("enter your marks = "))
mark  = (m >=60 and m>=90) 
print(mark)