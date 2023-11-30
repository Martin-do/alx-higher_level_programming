#!/usr/bin/python3
"""Function to find the peak in
	a list of numbers"""


def find_peak(list_of_integers):
    """finds the peak in a list of integers

	Args:
		list_of_integers (list): list of integers

	Returns:
		(int): highest number
	"""
    if not list_of_integers or len(list_of_integers) == 1:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if the peak is to the left or right of the middle element
        if mid > 0 and list_of_integers[mid] > list_of_integers[mid - 1]:
            right = mid - 1
        elif mid < len(list_of_integers) - 1 and list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            return mid

    return None
