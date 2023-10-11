#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    newList = set(my_list)
    for x in newList:
        sum += x
    return sum
