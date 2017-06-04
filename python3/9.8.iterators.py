xs = []
for x in xs:
    print(x)

"""
Desugared:
 
iterator = xs.iter()
try:
    while True:
        next(iterator)  # iterator.__next__()
except StopIteration:
    pass

This also means that any object that have these methods
can be looped over with a for loop.
"""


class Iter:
    class Iterator:
        def __next__(self):
            if hasattr(self, 'lol'):
                raise StopIteration
            self.lol = 'lul'
            return 666

        def __iter__(self):
            return self

    def __iter__(self):
        return Iter.Iterator()


for _ in Iter():
    print(_)

x = Iter()
iterator = x.__iter__()
for _ in iterator:
    print(_)

next(iterator, 'default')  # Suppresses StopIterator and returns 'default'
