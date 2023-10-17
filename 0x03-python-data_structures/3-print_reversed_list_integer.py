#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        my_list_reversed = reversed(my_list)
        for i in my_list_reversed:
            print("{:d}".format(i))
