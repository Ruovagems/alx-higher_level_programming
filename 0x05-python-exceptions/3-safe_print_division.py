#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b  # Attempt to perform the division
    except ZeroDivisionError:
        return (None)  # Handle division by zero
    except Exception as e:
        return (None)  # Handle other exceptions gracefully

    try:
        print("Inside result: {:.2f}".format(result))
    finally:
        return (result)
