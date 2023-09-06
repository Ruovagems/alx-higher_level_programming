#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for item in my_list:
            if count < x:
                print(item, end=" ")
                count += 1
        print()  # Print a new line after printing the elements
        return count
    except:
        return 0
