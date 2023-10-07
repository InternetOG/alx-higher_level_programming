#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    elif number > 0:
        number
    lastDigit = number % 10
    return print("{}".format(lastDigit))
