fib = 3

print(fib)
from fibo import *  # all names, except those that begin with _, overwrites names...
print(fib)

fib(666)


import fibo
import importlib
importlib.reload(fibo)  # Reload module
