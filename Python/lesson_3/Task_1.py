thesaurus = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
             'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
def num_translate(num):
    # if num.istitle()
    num_lower=num.lower()
    # if num_lower in thesaurus:
    trans = thesaurus.get(num_lower)
    if num.istitle():
        trans=trans.capitalize()
    print(trans)
num_translate(input())