#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit = number % 10
else:
    last_digit = number % -10

print("The last digit of {} is {}".format(number, last_digit), end='')

if last_digit > 5:
    print(" and is greater than 5")
elif l_digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
