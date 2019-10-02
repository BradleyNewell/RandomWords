import random
import re

file = open("words.txt", 'r')

blank = ''
for i in file:
    blank += i


def random_word():
    word = re.split('\n', blank)
    print(random.choice(word))


for i in range(5):
    random_word()