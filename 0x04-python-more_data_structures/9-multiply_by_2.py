#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for x in list(a_dictionary):
        new[x] = a_dictionary.get(x) * 2
    return new
