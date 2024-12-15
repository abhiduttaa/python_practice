# 3. Write a python program to find the roots of a quadratic equation.

import cmath
a= int(input("enter Number(a!=0)"))
b= int(input("enter Number"))
c= int(input("enter Number"))

d = (b**2) - (4 *a*c)

r1 = (-b + cmath.sqrt(d)) / (2 *a)
r2 = (-b - cmath.sqrt(d)) / (2 *a)

print("The Roots are = " , r1 , "and " , r2)

# # ?output:
# enter Number(a!=0)4
# enter Number2
# enter Number6
# The Roots are =  (-0.25+1.1989578808281798j) and  (-0.25-1.1989578808281798j)