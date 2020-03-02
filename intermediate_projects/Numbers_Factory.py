'''
You are given a two or more digits number N. For this mission, you should find the smallest positive number of X, such that the product of its digits is equal to N. If X does not exist, then return 0.

Let's examine the example. N = 20. We can factorize this number as 2*10, but 10 is not a digit. Also we can factorize it as 4*5 or 2*2*5. The smallest number for 2*2*5 is 225, for 4*5 -- 45. So we select 45.

Hints: Remember prime numbers (numbers divisible by only one) and be careful with endless loops.

Input: A number N as an integer.

Output: The number X as an integer.
'''

def checkio(number):
    results_unsorted = []

    for i in range(9,1,-1):
        while number%i == 0:
            results_unsorted.append(i)
            number = number / i
    if number != 1:
        return 0
    else:
        return int(''.join(str(i) for i in results_unsorted[::-1]))