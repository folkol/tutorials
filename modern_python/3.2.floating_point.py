1.1 + 2.2  # 3.3000000000000000003
1.1 + 2.2 == 3.3  # False

sum([0.1] * 10)  # .99999999999
sum([0.1] * 10) < 1  # True

from math import fsum

fsum([0.1] * 10) == 1.0  # True

38 / 5  # 7.6
38 // 5  # 7


from collections import defaultdict  # When key is missing, run factory function
d = {'raymond': 'red'}
e = defaultdict(lambda: 'black')

d['raymond']  # 'red'
# d['rachel']  # KeyError

e['raymond']  # 'red'
e['rachel']  # black

# Functions without arguments
set()
list()
dict()

d = defaultdict(set)
d['t'].add('tom')

d['m']  # Not KeyError, but set()
d['t'].add('tom')
d['t'].add('tim')
d['m'].add('martin')


# DefaultDict creates a new container to store elements with a common feature
from pprint import pprint

pprint(d)



d = defaultdict(list)
d['t'].append('tom')
d['t'].append('tom')

pprint(d)


names = ''' david betty susan mary darlene sandy davin
            shelly becky beatrice tom michael wallace'''.split()
d = defaultdict(list)
for name in names:
    feature = name[0]
    d[feature].append(name)

pprint(d)


d = defaultdict(list)
for name in names:
    feature = name[-1]
    d[feature].append(name)

pprint(d)


d = defaultdict(list)
for name in names:
    feature = len(name)
    d[feature].append(name)

pprint(d)


# SELECT name FROM names ORDER BY len(name)

pprint(sorted(names, key=len))

# Many functions take a key function ( x->y )


print(list(zip('abcdef', 'ghijlkm.....')))

from itertools import zip_longest
print(list(zip_longest('abcdef', 'ghijlkm.....')))   # (None, '.')...


m = [
    [10, 20],
    [30, 40],
    [50, 60],
]
# 3 rows by 2 columns

pprint(list(zip([10, 20], [30, 40], [50, 60])), width=15)
pprint(list(zip(*m)), width=15)

pprint(m, width=20)
for row in m:
    for col in row:
        print(col)

flattened = [x for row in m for x in row]  # Represents nested loops
# list(iterator)  Make list of any iterator
