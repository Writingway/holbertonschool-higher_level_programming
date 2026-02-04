#!/usr/bin/python3
"""

"""


class VerboseList(list):
    def append(self, item):
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, item):
        n_of_item = len(item)
        print("Extended the list with [{}] items.".format(n_of_item))
        super().extend(item)

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
