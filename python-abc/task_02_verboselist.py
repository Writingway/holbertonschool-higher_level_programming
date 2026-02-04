#!/usr/bin/python3
"""
A module that defines a VerboseList class which extends the built-in list
"""


class VerboseList(list):
    """
    A list subclass that prints messages on modifications.
    """
    def append(self, item):
        """
        Appends an item to the list and prints a message.
        """
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, item):
        """
        Extends the list with items from another iterable and prints a message.
        """
        n_of_item = len(item)
        print("Extended the list with [{}] items.".format(n_of_item))
        super().extend(item)

    def remove(self, item):
        """
        Removes an item from the list and prints a message.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Pops an item from the list at the given index and prints a message.
        """
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
