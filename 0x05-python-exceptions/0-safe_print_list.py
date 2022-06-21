def safe_print_list(my_list=[], x=0):
    count = 0
    while x != 0:
        try:
            print(my_list[x], end = "")
            count =+ 1
        except IndexError:
            continue
    return count