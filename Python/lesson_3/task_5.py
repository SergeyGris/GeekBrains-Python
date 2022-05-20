from random import choice
def get_jokes(n,nouns,adverbs,adjectives):
    list_of_jokes=[]
    for i in range(n):
        rand_noun = choice(nouns)
        rand_adverbs = choice(adverbs)
        rand_adjectives = choice(adjectives)
        list_of_jokes.insert(i,f'{rand_noun} {rand_adverbs} {rand_adjectives}')
    print(list_of_jokes)
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
n=int(input())
get_jokes(n,nouns,adverbs,adjectives)