#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def multiplyByNum(num):
        return num * number

    mapped = list(map(multiplyByNum, my_list))
    return mapped
