# 5. Реализовать функцию get_jokes(),
# возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def my_jokes(n):
    """returns n jokes of 3 words taken from 3 lists"""
    list1 = nouns[:]
    list2 = adverbs[:]
    list3 = adjectives[:]
    jok = []
    for i in range(n):
        noun = random.choice(list1)
        adverb = random.choice(list2)
        adjective = random.choice(list3)
        joke = f'{noun} {adverb} {adjective}'
        jok.append(joke)
    return jok


print(my_jokes(5))




