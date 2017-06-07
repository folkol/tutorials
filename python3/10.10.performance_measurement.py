from timeit import Timer

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

import profile


def f():
    for x in range(666):
        print(x)


profile.run('f()')
