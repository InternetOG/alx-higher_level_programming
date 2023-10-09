#!/usr/bin/python3
def fizzbuzz():
    for fz in range(1, 101):
        if fz % 3 == 0 and fz % 5 == 0:
            print("{}".format("FizzBuzz"), end=" ")
        elif fz % 3 == 0:
            print("{}".format("Fizz"), end=" ")
        elif fz % 5 == 0:
            print("{}".format("Buzz"), end=" ")
        else:
            print("{}".format(fz), end=" ")
