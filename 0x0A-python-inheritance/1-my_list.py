#!/usr/bin/python3


class MyList(list):
    """creates a sorted list in ascending order
    Args:
        self.list (list): list not sorted
    """
    def print_sorted(self):
        ls = self[:]
        for i in range(len(ls)):
            if (i + 1) < len(ls):
                if ls[i] > ls[i+1]:
                    ls[i], ls[i+1] = ls[i+1], ls[i]

        print(ls)
