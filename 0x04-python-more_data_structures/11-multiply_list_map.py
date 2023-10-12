#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    myListCpy = my_list.copy()
    mul = map(lambda eachNum: number * eachNum, myListCpy)
    mulList = list(mul)
    return mulList
