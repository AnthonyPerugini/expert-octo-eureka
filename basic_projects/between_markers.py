"""
You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.

This is a simplified version of the Between Markers mission.

The initial and final markers are always different.
The initial and final markers are always 1 char size.
The initial and final markers always exist in a string and go one after another.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.

Example:

between_markers('What is >apple<', '>', '<') == 'apple'
1
How it is used: For text parsing.

Precondition: There can't be more than one final and one initial markers.
"""


# MY SOLUTION
# input string, initial, final
def between_markers(data: str, initial: str, final:str):
# find the index of the initial symbol
# find the index of the final symbol
# Slice the string at [initial index + 1: final index]
    return data[data.find(initial) + 1: data.find(final)]



# HARDER BETWEEN MARKERS TASK:

"""
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two 
markers. But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.

Example:

between_markers('What is >apple<', '>', '<') == 'apple'
between_markers('No[/b] hi', '[b]', '[/b]') == 'No'
1
2
How it is used: for parsing texts

Precondition: can't be more than one final marker and can't be more than one initial. Marker can't be an empty string"""

# MY SOLUTION
# input string, initial, final
def between_markers(data: str, initial: str, final:str):

# find the index of the initial symbol
    initial_index = data.find(initial)
# if initial_index isn't found (-1), then set to 0
    if initial_index == -1:
        initial_index = 0
        lenInitial = 0
    else:
        lenInitial = len(initial)
# find the index of the final symbol
    final_index = data.find(final)
# if final_index isn't found (-1), then set to len(data)
    if final_index == -1:
        final_index = len(data)
# Slice the string at [initial index + 1: final index]
    return data[initial_index + lenInitial: final_index]

# BETTER SOLUTION:
def better_between_markers(text: str, begin: str, end: str) -> str:
    try:
        beginIndex=text.index(begin)+len(begin)
    except:
        beginIndex=0
    try:
        endIndex=text.index(end)
    except:
        endIndex=len(text)
    return text[beginIndex:endIndex]