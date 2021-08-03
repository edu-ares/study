"""Make a bar chart of the letters of an input, each letter being a unit of the bar."""
import pprint
from collections import defaultdict

alphabet = list('abcdefghijklmnopqrstuvwyz')
bar_dict = defaultdict(list)

sentence = input("Write a sentence to be divided in letters.\n>").lower()

#optimized thanks to an anonymous suggestion
for letter in sentence:
    if letter.isalpha():
        bar_dict[letter].append(letter)
pprint.pprint(bar_dict, width=110)
