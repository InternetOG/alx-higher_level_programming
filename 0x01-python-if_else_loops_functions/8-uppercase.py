#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if s is not None:
            if s >= chr(97) and s <= chr(123):
                print("{}".format(chr(ord(s) - 32)), end="")
            else:
                print("{}".format(s), end="")
    else:
        print("\n")
