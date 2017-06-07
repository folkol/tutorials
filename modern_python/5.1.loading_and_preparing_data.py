# defaultdict for accumulating/tabulating data

from collections import defaultdict
from pprint import pprint

d = defaultdict(list)
d['raymond'].append('red')
d['rachel'].append('blue')
d['mattew'].append('yellow')

pprint(d)

d['raymond'].append('mac')
d['rachel'].append('pc')
d['mattew'].append('vtech')

data = dict(d)

# defaultdict can be used for grouping, accumulation

# Model one-to-many: dict(one, list_of_many)

e2s = {
    'one': ['uno'],
    'two': ['dos'],
    'three': ['tres'],
    'trio': ['tres'],
    'free': ['libre', 'gratis']
}

pprint(e2s, width=40)

s2e = defaultdict(list)
for eng, spanish in e2s.items():
    for span in spanish:
        s2e[span].append(eng)

pprint(dict(s2e))

e2s_one_to_one = dict(one='uno', two='dos', three='tres')
s2e_one_to_one = {value: key for key, value in e2s_one_to_one.items()}  # Invert bijection
pprint(s2e_one_to_one)

import glob

glob_glob = glob.glob('rhettiger/congress_data/*csv')  # Global wildcard expansion -> os.expand_wildcard()
pprint(glob_glob)

with open('rhettiger/congress_data/congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    print(f.read())

it = iter('abcdefg')
next(it)
next(it)
list(it)  # ['c', 'd', 'e', 'f', 'g']

import csv

with open('rhettiger/congress_data/congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    for row in csv.reader(f):
        print(row)

t = 'Raymond', 'Hettinger', 54, 'python@rcn.com'  # rside -> packing
len(t)  # 4

fname, lname, age, email = t  # lside -> unpacking
print(lname)

names = 'ramond rachel matthew'.split()
colors = 'red blue yellow'.split()
cities = 'austin dallas austin houston chicago dallas austin'.split()

# Loop idioms
for i in range(len(names)):
    print(names[i].upper())

for name in names:
    print(name.upper())

for i in range(len(names)):
    print(i + 1, names[i])

for i, name in enumerate(names, start=1):
    print(i, name)


for i in range(len(colors) - 1, -1, -1):
    print(colors[i])

for color in reversed(colors):
    print(color)


n = min(len(names), len(colors))
for i in range(n):
    print(names[i], colors[i])

for name, color in zip(names, colors):
    print(name, color)


for color in sorted(colors):
    print(color)

for color in sorted(colors, key=len):
    print(color)


for city in set(cities):
    print(city)

for city in sorted(set(cities)):
    print(city)

# SELECT DISTINCT(city) FROM cities ORDER BY city;

for city in reversed(sorted(set(cities))):
    print(city)

for i, city in enumerate(reversed(sorted(set(cities)))):
    print(i, city)

for i, city in enumerate(map(str.upper, reversed(sorted(set(cities))))):
    print(i, city)


import collections
c = collections.Counter()
c['red'] += 1  # Not a KeyError
c['blue'] += 1
c['blue'] += 1

pprint(c)

pprint(c.items())
pprint(list(c.elements()))


print(c.most_common(1))
print(c.most_common(2))

assert 5 + 3 == 7, 'custom message'
