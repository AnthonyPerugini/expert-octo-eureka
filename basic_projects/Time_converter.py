'''
Input: Time in a 24-hour format (as a string).

Output: Time in a 12-hour format (as a string).
'''


def time_converter(time: str):

    is_am = "a.m."
    #Break input string into hh and mm
    hh = int(time.split(":")[0])
    mm = time.split(":")[1]
    #if hh > 12, set to PM and if hh > 13 subtract 12 from hh
    if hh >= 12:
        is_am = "p.m."
    if hh >= 13:
        hh -= 12
    if hh == 0:
        hh = 12

    return f'{hh}:{mm} {is_am}'

print(time_converter("12:30"))