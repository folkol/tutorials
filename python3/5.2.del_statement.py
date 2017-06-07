x = 3
print(x)
del x
# print(x)  # NameError: name 'x' is not defined

xs = [1, 2, 3, 4, 5, 6, 7]
print(xs)
del xs[:1]
print(xs)
del xs[2:4]
print(xs)
del xs[:]
print(xs)
del xs
# print(xs)  # name 'xs' is not defined

xs = list(range(10))
print(xs)
xs[:] = []  # Replace slice [:] with []
print(xs)  # Empty


xs = list(range(10))
print(xs)
del xs
# print(xs)  # NameError: name 'xs' is not defined
