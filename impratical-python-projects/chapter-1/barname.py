import pprint

alphabet = list('abcdefghijklmnopqrstuvwyz')
bar_dict = {}

sentence = input("Write a sentence to be divided in letters.\n>").lower()
sentence_splited = list(sentence)

for letter in alphabet:
    bar = []
    n_of_times = sentence_splited.count(letter)
    while n_of_times > 0:
        bar.append(letter)
        n_of_times = n_of_times -1
    if bar != []:
        bar_dict[letter] = bar

pprint.pprint(bar_dict)