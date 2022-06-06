#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for x in my_string:
        if x != 'c' or x != 'C':
            str = str + x
return str

