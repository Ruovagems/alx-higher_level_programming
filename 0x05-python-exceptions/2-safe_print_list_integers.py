def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            if count >= x:
                break  # Exit the loop when x elements have been printed
            try:
                # Attempt to convert the item to an integer and print it
                formatted_item = "{:d}".format(int(item))
                print(formatted_item, end=" ")
                count += 1
            except (ValueError, TypeError):
                pass  # Skip non-integer items silently
        print()  # Print a new line after printing the integers
        return (count)
    except TypeError:
        return (0)
