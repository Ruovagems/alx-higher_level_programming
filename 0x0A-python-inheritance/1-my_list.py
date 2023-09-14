#!/usr/bin/python3
class MyList(list):
    """A custom list class that inherits from the built-in list class.
    
    Args:
        list: class list

    """

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
