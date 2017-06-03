fib = 3

print(fib)
from fibo import *  # all names, except those that begin with _, overwrites names...
print(fib)

fib(666)

print('import fibo')
import fibo
print('import importlib')
import importlib
print('reload')
importlib.reload(fibo)  # Reload module
