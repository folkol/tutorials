xs = (i * i for i in range(10))

print(type(xs))  # <class 'generator'>

next(xs)
next(xs)
next(xs)
assert next(xs) == 9


assert 5 == sum(i * i for i in range(3))
