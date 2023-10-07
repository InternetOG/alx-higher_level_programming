#!/usr/bin/python3
def uppercase(str):
    newStr = ""
    for s in str:
        if s is not None:
            if s >= chr(97) and s <= chr(122):
                newStr += chr(ord(s) - 32)
            else:
                newStr += s
    print("{}".format(newStr))
