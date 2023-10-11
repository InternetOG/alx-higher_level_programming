#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDic = a_dictionary.copy()
    for k in a_dictionary:
        newDic[k] *= 2
    return newDic
