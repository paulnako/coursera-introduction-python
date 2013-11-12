# -*- coding:utf-8 -*-

def is_ascending(numbers):
    """Returns whether the given list of numbers is in ascending order."""
    for i in range(len(numbers)):
        if numbers[i+1] < numbers[i]:
            return False
    return True


print is_ascending([1, 3, 5, 7])
