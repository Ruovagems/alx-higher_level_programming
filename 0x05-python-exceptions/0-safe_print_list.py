#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    total = 0
    for i in range(x):
        if i < len(my_list):
            print(f"{my_list[i]}", end="")
            total += 1
        else:
            break
    print()
    return total
