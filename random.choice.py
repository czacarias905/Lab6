#Cecilia Zacarias
#2/20/2020

#random.choice
#problem #3 select a day of the week from a list and print that day.

import random

day_list = ["monday","tuesday","wenday","thursday","friday","saturday","sunday"]

print("A random day of the week is :")
print(random.choices(day_list,weights=None,cum_weights=None,k=1))

