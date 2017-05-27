print('Hello, world!')

import sys
sys.stdout.write('Hello, world!\n')

x = ('Hello', 'World')
print(str(x), repr(x))
y = 'Hello, world!'
print(str(y), repr(y))



for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


print('12'.zfill(5))

print('-3.14'.zfill(7))

print('3.14159265359'.zfill(5))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))

print('Jack: {0[Jack]:d}'.format(table))
def f(Jack, Dcab, **kwargs):
    print(locals())
f(**table)
print('Jack: {Jack}'.format(**table))
print('Jack: {Jack:d}'.format(Jack=4098))
