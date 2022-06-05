#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    count1 = len(tuple_a)
    count2 = len(tuple_b)
    new = ()
    while (count1 < 2 or count2 < 2):
        tuple_a += (0,)
        tuple_b += (0,)
        count1 += 1
        count2 += 1
    for x in range(0, 2):
        new += (tuple_a[x]+tuple_b[x],)
    return new
