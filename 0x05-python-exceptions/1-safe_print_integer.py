def safe_print_integer(value):
    try:
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        print()  # Print a new line
        return (True)
    except (ValueError, TypeError):
        return (False)
