from typing import *

x = 1
y = '1'  # type: int
z: int = '10'


def f(x: int, y: int) -> int:
    return x + y


f(2, 4)
# f(10, 'hello')

from collections import OrderedDict, deque

w = {}


def g(x: OrderedDict):
    pass


g(w)


def h(xs: Sequence):  # Indexable, Iterable
    print(len(xs))
    print(xs[0])
    for i in xs:
        print(i)
    print()


h([10, 20, 30])
h('foo')
h((11, 12, 13))
h(None)


def i(xs: Sequence[int]):  # Indexable, Iterable
    print(len(xs))
    print(xs[0])
    for i in xs:
        print(i)
    print()


i([10, 20, 30])
i('foo')
i((11, 12, 13))


# i(None)


def j(xs: List[int]) -> None:
    print(len(xs))
    print(xs[0])
    for i in xs:
        print(i)
    print()


j([10, 20, 30])
j('foo')
j((11, 12, 13))
j(None)

heights = [97.1, 102.5, 97.5]  # type: List[float]
person = ('Raymond', 5 * 12 + 11)  # type: Tuple[str, float]
info = ('Pearson', 'Course', 'Python', 'Raymond')  # type: Tuple[str, ...]


def k(x: int, y: Optional(int) = None) -> int:
    if y is None:
        y = 20
    return x + y


fifo1 = deque()  # type: Deque[int] doesn't work :(
fifo2 = deque()  # type: deque

print(f'The answer is {x} today.')


# mypy
# pyflakes
# hypothesis
# unittest -> node py.test


from collections import namedtuple

# Point = namedtuple('Point', [('x', int), ('y', int)])
Point = namedtuple('Point', ['x', 'y'])
point = Point(74, 'foo')

print(point)
