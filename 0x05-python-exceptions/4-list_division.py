#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    my_list = []
    while count < list_length:
        try:
            res = my_list_1[count] / my_list_2[count]
        except ValueError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            my_list.append(res)
    return my_list