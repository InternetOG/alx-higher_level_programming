#!/usr/bin/python3
for x in range(00, 100):
    if x is len(range(0, 100)) - 1:
        print("{:02}".format(x))
    else:
        print("{:02}".format(x), end=", ")
