#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_cpy = my_list.copy()
    if idx < 0:
        if idx < (len(my_list) * -1):
            return my_list_cpy
        my_list_cpy[idx] = element
        return my_list_cpy
    elif idx > len(my_list):
        return my_list_cpy
    else:
        my_list_cpy[idx] = element
        return my_list_cpy
