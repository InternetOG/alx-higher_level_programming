#!/usr/bin/python3
def islower(c):
    if c is not None:
        if c >= chr(97) and c <= chr(122):
            return True
        else:
            return False
