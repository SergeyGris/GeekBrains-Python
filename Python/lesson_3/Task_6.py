from random import sample
from random import shuffle


def get_jokes(n, nouns, adverbs, adjectives):
    list_of_len=[len(nouns),len(adverbs),len(adjectives)]
    if n>min(list_of_len):
        print('Превышено количество шуток=)')
        return None
    else:
        list_of_jokes = []
        rand_noun = sample(nouns, n)
        rand_adverbs = sample(adverbs, n)
        rand_adjectives = sample(adjectives, n)
        for noun, adverb,adjective in zip(rand_noun,rand_adverbs,rand_adjectives):
            list_of_jokes.append(f'{noun} {adverb} {adjective}')
        print(list_of_jokes)
        return(list_of_jokes)



nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
n = int(input())
get_jokes(n, nouns, adverbs, adjectives)
