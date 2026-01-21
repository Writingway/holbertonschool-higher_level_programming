#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 1:
        x = tuple_a[0]
    else:
        x = 0
    if len(tuple_a) >= 2:
        y = tuple_a[1]
    else:
        y = 0
    if len(tuple_b) >= 1:
        a = tuple_b[0]
    else:
        a = 0
    if len(tuple_b) >= 2:
        b = tuple_b[1]
    else:
        b = 0
    return (x + a, y + b)
