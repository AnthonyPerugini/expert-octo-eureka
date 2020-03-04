"""
In this mission your task is to determine the popularity of certain words in the text.

At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need
to determine.

When solving this task pay attention to the following points:

The words should be sought in all registers. This means that if you need to find a word "one" then words like "one",
"One", "oNe", "ONE" etc. will do.
The search words are always indicated in the lowercase.
If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.
Input: The text and the search words array.

Output: The dictionary where the search words are the keys and values are the number of times when those words are
occurring in a given text.

Example:

popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
    'i': 4,
    'was': 3,
    'three': 0,
    'near': 0
}

Precondition:
The input text will consists of English letters in uppercase and lowercase and whitespaces.
"""


# MY SOLUTION
# input popular words, and data string
def popular_words(data: str, pop_words: list) -> hash:
#   Create an empty results_dict
    resultsHash = {}
#   Split data into list of words, separated at blank spaces
    listOfWords = data.lower().split()

#   for each word in the split data (lowercase),
    for word in listOfWords:
# 	    if that word is in popular_words (already lowercase),
        if word in pop_words:
# 		    append that word to the results_dictionary
            if word in resultsHash:
                resultsHash[word] += 1
#           if it doesnt exist / add +1 to counter
            else:
                resultsHash[word] = 1

#   check if all the pop_words are in the resultsHash, if not add a 0 count to the hash
    for word in pop_words:
        if word not in resultsHash:
            resultsHash[word] = 0

    return resultsHash



# Better solution
def better_popular_words(text, words):
    my_dict = {}
    text = [i.lower() for i in text.split()]
    for word in words:
        my_dict[word] = text.count(word)

    return my_dict

