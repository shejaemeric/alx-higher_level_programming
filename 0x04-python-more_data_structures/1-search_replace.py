#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for x in my_list:
        new.append(replace if x == search else x)
    return new
