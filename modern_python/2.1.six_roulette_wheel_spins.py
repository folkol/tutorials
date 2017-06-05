from random import *
from statistics import *
from collections import *

# Six roulette wheels -- 18 red slots, 18 black slots and 2 green slots

choice(['red', 'red', 'red', 'black', 'black', 'green'])  # ...

choice(['red'] * 18 + ['black'] * 18 + ['green'] * 2)

population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
choice(population)
[choice(population) for i in range(6)]

choices(population, k=6)
print(Counter(choices(population, k=6)))

choices(['red', 'black', 'green'], [18, 18, 2], k=6)

print(Counter(choices(['red', 'black', 'green'], [18, 18, 2], k=6)))
