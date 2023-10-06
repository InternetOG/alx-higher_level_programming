#!/usr/bin/python3
def islower(c):
    if c is not None:
        if chr(97) <= c <= chr(122):
            return True
        else:
            return False
