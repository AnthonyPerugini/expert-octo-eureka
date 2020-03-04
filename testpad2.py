myfile = open('data.txt', 'w')
myfile.write("testtest /n test")
myfile.close()

# TODO

def Eulers():
    c = 0
    for i in range(1, 1000):
        if i % 3 == 0:
            c += i
        elif i % 5 == 0:
            c += i
        return c


def duplicates(iterable) -> list:
    l = []
    for item in iterable:
        if iterable.count(item) > 1:
            if item not in l:
                l.append(item)
    return l

list1 = [1,2,3,3,2,1,5,6,1,2]
l = []
[l.append(item) for item in list1 if list1.count(item) > 1 and item not in l]


li, li2 = ['f','g','h','t','e'], ['f','g','h','t','e']



for i, color in enumerate(li):
    print(i, '--->', color)

d = {'g': '2', 'f': '2', 's': '2', 'a': '2', 'c': '2', 'j': '2'}

for k, v in d.items():
    print(k, '--->', v)

from collections import defaultdict as dd


from functools import partial
partial()


def gfg_decorator():
    pass

@gfg_decorator
def hello_decorator():
    print("Gfg")

'''
Git Test.  This comment was added to the Master
'''
