#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
n = number
rem = n % 10
if rem > 5:
    if n < 0:
        print(f"Last digit of {n} is -{-n % 10} and is greater than 5")
    else:
        print(f"Last digit of {n} is {rem} and is greater than 5")
elif rem == 0:
    print(f"Last digit of {n:d} is {rem:d} and is 0")
elif rem < 6:
    if number < 0:
        print(f"Last digit of {n} is -{-n % 10} and is less than 6 and not 0")
    else:
        print(f"Last digit of {n:d} is {rem:d} and is less than 6 and not 0")
