#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    xorElement = set_1 ^ set_2
    sortElement = sorted(xorElement)
    return sortElement
