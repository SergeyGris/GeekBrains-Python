thesaurus = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
             'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
def num_translate(num):
    # if num.istitle()
    num_lower=num.lower()
    if num_lower in thesaurus:
        trans = thesaurus[num_lower]
        if num.istitle():
            trans.capitalize()
        print(trans)
    else:
        print(None)
num_translate(input())