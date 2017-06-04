def f():
    for i in ['foo', 'bar', 666]:
        yield i
    return 'Done'  # Message for the StopIteration


xs = f()
print(xs)  # <generator object f at 0x10519e620>
print(type(xs))  # <class 'generator'>
assert hasattr(xs, '__next__')
assert hasattr(xs, '__iter__')

print(next(xs))  # 'foo'
print(next(xs))  # 'foo'
print(next(xs))  # 'foo'
# print(next(xs))  # StopIteration 'Done'
