#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keyValuePairs = a_dictionary.items()
    sortedList = sorted(keyValuePairs)
    for k, v in sortedList:
        print("{}: {}".format(k, v))
