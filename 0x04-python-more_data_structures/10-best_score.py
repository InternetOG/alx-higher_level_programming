#!/usr/bin/python3
def best_score(a_dictionary):
    arr = []
    for k, v in a_dictionary.items():
        arr.append(v)
    maxNum = max(arr)
    for k, v in a_dictionary.items():
        if a_dictionary[k] == maxNum:
            return k
