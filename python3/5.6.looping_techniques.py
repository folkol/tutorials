knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

print(zip([1, 2, 3], ['a', 'b', 'c']))  # 'zipobject'...
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))  # [(1, 'a'), (2, 'b'), (3, 'c')]

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}'.format(q, a))

for q, a in zip(questions, answers):
    print(f'What is your {q}? It is {a}')

for i in reversed(range(1, 10, 2)):
    print(i)

print(reversed([1, 2, 3]))  # list_reversed_iterator
print(list(reversed([1, 2, 3])))  # [3, 2, 1]


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
print(basket)
print(sorted(basket))


import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.6, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

print(x for x in raw_data if not math.isnan(x))
print((x for x in raw_data if not math.isnan(x)))
print({x for x in raw_data if not math.isnan(x)})
print([x for x in raw_data if not math.isnan(x)])
