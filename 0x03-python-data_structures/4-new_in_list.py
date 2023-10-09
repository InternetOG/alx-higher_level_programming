#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if len(my_list) > 0:
        my_list_cpy = my_list.copy()
        if idx < 0:
            if (idx < 0) and (idx >= (len(my_list) * -1)):
                my_list_cpy[idx] = element
                return my_list_cpy
            else:
                return my_list_cpy
        elif idx >= len(my_list):
            return my_list_cpy
        elif idx >= 0 and idx < len(my_list):
            my_list_cpy[idx] = element
            return my_list_cpy
    else:
        return None
