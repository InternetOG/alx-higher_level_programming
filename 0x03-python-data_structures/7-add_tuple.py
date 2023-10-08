#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sumi = []
    for x in range(len(tuple_a)) and range(len(tuple_b)):
        sumi.append(tuple_a[x] + tuple_b[x])
    return tuple(sumi)
