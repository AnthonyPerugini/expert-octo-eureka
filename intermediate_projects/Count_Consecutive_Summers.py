'''
Positive integers can be expressed as sums of consecutive positive integers in various ways. For example, 42 can be expressed as such a sum in four different ways:(a) 3+4+5+6+7+8+9, (b) 9+10+11+12, (c) 13+14+15 and (d) 42. As the last solution (d) shows, any positive integer can always be trivially expressed as a singleton sum that consists of that integer alone.

Compute how many different ways it can be expressed as a sum of consecutive positive integers.

Input: Int.

Output: Int.
'''

def Count_Consecutive_Summers(target):
    count = 0
    sum = 0
    data_set = list(range(1,target+1))
    while data_set:
        for i in data_set:
            sum += i
            if sum > target:
                sum = 0
                data_set.pop(0)
                break
            elif sum == target:
                sum = 0
                count += 1
                data_set.pop(0)
                break
    return count


print(Count_Consecutive_Summers(99))