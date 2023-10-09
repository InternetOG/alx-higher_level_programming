#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        list_result = []
        for x in my_list.copy():
            list_result.append(True if x % 2 == 0 else False)
        return list_result


