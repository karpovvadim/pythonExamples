"""
cycle: позволяет бесконечно перебирать итератор;
"""
import itertools
count = 0
letters = {'А', 'В', 'С'}
for letter in itertools.cycle(letters):
    print(letter)
    count += 1
    if count > 100:
        break
