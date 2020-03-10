"""
You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, a dot or space.
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
Input: A string.

Output: A string.

Example:

first_word("Hello world") == "Hello"
first_word("greetings, friends") == "greetings"
1
2
How it is used: the first word is a command in a command line

Precondition: the text can contain a-z A-Z , . '
"""


def first_word(data: str) -> str:
    data = data.strip(",. ")
    for char in data:
        if char == "." or char == ",":
            data = data.replace(char, " ")
    return data.split(" ")[0]

first_word("Hello") == "Hello"




