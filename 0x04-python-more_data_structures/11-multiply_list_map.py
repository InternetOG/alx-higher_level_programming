#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    mul = map(lambda eachNum: number * eachNum, my_list)
    mulList = list(mul)
    return mulList
