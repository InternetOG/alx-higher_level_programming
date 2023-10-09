#!/usr/bin/python3
def no_c(my_string):
    newStr = ""
    for char in my_string:
        if char == "c" or char == "C":
            continue
        else:
            newStr += char
    return newStr
