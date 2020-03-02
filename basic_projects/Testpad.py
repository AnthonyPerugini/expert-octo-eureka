phrase = "mary had a little lamb"

def extract_longer(length, sentence):
    final = []
    for word in phrase.split():
        if len(word) >= length:
            final.append(word)
    if not final:
        return False
    return final


print(extract_longer(9, phrase))


matrix = [[0 for col in range(4)] for row in range(3)]


class Person(object):
    species = 'Homo sapien'

    def __init__(self, name='unknown', age='18'):
        self.name = name
        self.age = age

    def talk(self):
        return f'hello there, my name is {self.name}'

class Query(object):

    def __init__(self, classification= 'FVEY', justification= 'Primary email address of GOVT', selector= 'test@govt.gov'):
        self.classification = classification
        self.justification = justification
        self.selector = selector

    def __str__(self):
        return f'<classification= {self.classification}, justification= {self.justification}, selector= {self.selector}>'

class RangedQuery(Query):
    def __init__(self, classification, justification, selector):
        super(Query, self).__init__(classification,justification,selector)






