'''
You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the non-unique
elements in this list. To do so you will need to remove all unique elements (elements which are contained in a given list only once). 4
When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and
result will be [1, 3, 1, 3].

Input: A list of integers.

Output: An iterable of integers.
'''

'''
# MY FIRST ATTEMPT:
def checkio(list):
    count = 0
    final = []
    for i in list:
        for j in list:
            if i == j:
                count += 1
        if count >= 2:
            final.append(i)
        count = 0
    return final
'''
# BETTER SOLUTION:
def checkio(data: list) -> list:
    for i in data[::-1]:
        if data.count(i) == 1:
            data.remove(i)
    return data
print(checkio([5,5,3,4,6]))