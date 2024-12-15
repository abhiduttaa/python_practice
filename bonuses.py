# 5. Write a program to calculate bonuses for employees based on grade and basic pay. (Given # name, grade, basic pay, dearness allowance, HRA, CCA, conveyance, etc.)

name = input("Enter the Emplayee's Name =")

grade = input("Enter the Emplayee's grade(A, B ,C) =")

basicpay = float(input("Enter the Emplayee's Basic Pay ="))

da = basicpay * (40 /100)
hra = basicpay * (20 /100)
cca = 1000
Conveyance = 2000

if grade == "A":
    bonus = basicpay * (10/100)
elif grade == "B":
    bonus = basicpay * (7/100)
elif grade == "C":
    bonus = basicpay * (5/100)
else:
    print("No Increment")

total = basicpay + da + hra + cca + Conveyance + bonus 

print("Emplayee's Name =" ,name)
print("Emplayee's grade =" ,grade)
print("Emplayee's basicpay =" ,basicpay)
print("Emplayee's da =" ,da)
print("Emplayee's hra =" ,hra)
print("Emplayee's cca =" ,cca)
print("Emplayee's Conveyance =" ,Conveyance)
print("Emplayee's  bonus=" ,bonus)
print("Emplayee's  total=" ,total)
