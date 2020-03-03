'''
Stephen's speech module is broken. This module is responsible for his number pronunciation. He has to click to input all of the 
numerical digits in a figure, so when there are big numbers it can take him a long time. Help the robot to speak properly and increase 
his number processing speed by writing a new speech module for him. All the words in the string must be separated by exactly one space character. 
Be careful with spaces -- it's hard to see if you place two spaces instead one.

Input: A number as an integer.

Output: The string representation of the number as a string.
'''


under_20 = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def checkio(number):
    if number < 20:
        return under_20[number]
    elif number < 100:
        if (number % 10) == 0:
            return tens[(number // 10) - 2]
        else:
            return tens[(number // 10) - 2] + " " + under_20[number % 10]
    else:
        if (number % 100) == 0:
            return under_20[number // 100] + " hundred"
        elif (number % 100 < 20):
            return under_20[(number // 100)] + " hundred " + under_20[number % 100]
        else:
            if number % 10 == 0:
                return under_20[(number // 100)] + " hundred " + tens[(((number % 100) - (number % 10)) // 10 - 2)]
            else:
                return under_20[(number // 100)] + " hundred " + tens[(((number % 100) - (number % 10)) // 10 - 2)] + " " + under_20[number % 10]

print(checkio(312))
