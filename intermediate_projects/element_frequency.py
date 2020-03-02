"""
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times
they appear in elements. If two elements have the same frequency, they should end up in the same order as the first
appearance in the iterable.

Input: Iterable

Output: Iterable

example:
frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']

"""
from collections import Counter

def element_frequency(data: list):
    return [n for n, count in Counter(data).most_common() for i in range(count)]

t = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5, 5, 4, 4, 4, 4, 4, 4]
print(element_frequency(t))