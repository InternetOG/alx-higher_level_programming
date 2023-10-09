#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    sumi = []
    if len(b) == 0:
        b = [0, 0]
    elif len(b) < 2:
        b.append(0)
    if len(a) == 0:
        a = [0, 0]
    elif len(a) < 2:
        a.append(0)
    for x in range(2):
        sumi.append(a[x] + b[x])
    return tuple(sumi)
