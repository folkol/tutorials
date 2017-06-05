#   %-formatting    .format     f''
x = 10
print('The answer is %d today.' % 10)
print('The answer is {0} today.'.format(x))
print('The answer is {x} today.'.format(x=x))
print(f'The answer is {x} today.')  # Compiled, not evaled
print(f'The answer is {x :08d} today.')
print(f'The answer is {x ** 2 :08d} today.')

# raise ValueError(f"Expected {x!r} to a float not a {type(x).__name__}.")

# d = {}
# d['dragons']  # KeyError: 'dragons'

from collections import Counter  # Smalltalk 'Bags', C++ Multiset

d = Counter()
d['dragons']  # 0
d['dragon'] += 1

xs = Counter('red green red blue blue green'.split())
xs.most_common()  # [('red', 2), ('green', 2), ('blue', 2)]
xs.most_common(1)  # [('red', 2)]

list(xs.elements())  # ['red', 'red', 'green', 'green', 'blue', 'blue']
xs.keys()  # dict_keys(['red', 'green', 'blue'])
xs.values()  # dict_values([2, 2, 2])

from statistics import mean, median, mode, stdev, pstdev

mean([50, 52, 53])
median([50, 53, 53])
median([51, 50, 53, 53])
stdev([51, 50, 52, 53, 51, 51])
pstdev([51, 50, 52, 53, 51, 51])

s = [10, 20, 30]
t = [40, 50, 60]
u = s + t
u

u[:2]

s = 'abracadabra'
i = s.index('c')  # 4

s = [10, 5, 70, 2]
s.sort()  # in place
sorted(s)  # returns new list

# lambda -> partial objects, itemgetters, attrgetters, etc

100 + (lambda x: x ** 2)(5) + 50  # 175

(lambda x, y: 3 * x + y)(1, 2)

x = 10
y = 20
f = lambda: x + y  # deferred computation, promises, freeze_and_thaw etc

print(f())

x = 15
x > 6  # True
x < 10  # False

x > 6 and x < 20
6 < x < 20  # Chained comparison

from random import *

seed(666)
random()
random()
random()

uniform(1000, 1100)
triangular(1000, 1100)
gauss(100, 15)  # IQs, Normal Distribution

expovariate(20)

from statistics import mean, stdev

mean([triangular(1000, 1100) for i in range(1000)])

data = [triangular(1000, 1100) for i in range(1000)]
mean(data)
stdev(data)

from random import choice, choices, random, shuffle

xs = ['win', 'lose', 'draw', 'play again', 'double win']
choice(xs)  # equidistributed

choices(xs, 10)  #

from collections import Counter

Counter(choices(xs, k=10))
Counter(choices(xs, [5, 4, 3, 2, 1], k=10))  # weights

shuffle(xs)  # in place
choices(xs, k=5)

sample(xs, 6)  # Without replacement
sorted(sample(range(1, 50), k=6))


sample(xs, k=1)  # ['win']
choice(xs)  # 'win'

shuffle(xs)

sample(xs, k=len(xs))


