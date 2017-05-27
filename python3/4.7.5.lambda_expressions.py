from operator import itemgetter


def make_foo():
    return lambda a, b: a + b


foo = make_foo()
print(foo(2, 3))


def f(k):
    return lambda x: x + k


bar = f(42)
print(bar(0))
print(bar(10))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(pairs)
pairs.sort(key=lambda pair: pair[1])
print(pairs)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(pairs)
pairs.sort(key=itemgetter(1))
print(pairs)
