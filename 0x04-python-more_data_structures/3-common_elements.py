#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_element = set_1 & set_2
    toList = list(common_element)
    return toList
