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

# Another suggestion from the person that helped was to use Counter to solve the problem
# from collections import Counter
# import string
# counts = Counter(input().upper())
# for letter in string.ascii_uppercase:
#     if counts[letter]:
#         print(letter * counts[letter])
