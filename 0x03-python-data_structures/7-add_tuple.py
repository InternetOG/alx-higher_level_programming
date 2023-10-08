#!/usr/bin/python3
arr = []


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 0:
        return tuple_a
    for x in range(len(tuple_b)):
        if len(tuple_b) >= 2:
            addTp = tuple_a[x] + tuple_b[x]
            arr.append(addTp)
        elif len(tuple_b) < 2 and len(tuple_b) == 1:
            addTp = tuple_a[x] + tuple_b[x]
            arr.append(addTp)
            x += 1
            addTp = tuple_a[x] + 0
            arr.append(addTp)
    return tuple(arr)


