#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    l_dig = number % -10
elif (number >= 0):
    l_dig = number % 10
if (l_dig > 5):
    print(f"Last digit of {number} is {l_dig} and is greater than 5")
elif (l_dig == 0):
    print(f"Last digit of {number} is {l_dig} and is 0")
else:
    print(f"Last digit of {number} is {l_dig} and is less than 6 and not 0")
