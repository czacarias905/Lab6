#Cecilia Zacarias
#2/20/2020

#factorial.py
#Problem #6 this program calculates the factorial of a user input x value with a for statement.

import math

num = int(input("enter a number: "))

fac = 1

for i in range(1, num + 1):
    fac = fac* i

print("factorial of", num,"is", fac)
