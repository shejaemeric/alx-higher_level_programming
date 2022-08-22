#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        a_list = list(a_dictionary)
        count = len(a_list)
        max = a_dictionary.get(a_list[0])
        res = a_list[0]
        for x in a_list[1:count]:
            next = a_dictionary.get(x)
            if next > max:
                max = next
                res = x
        return(res)
    else:
        return None
