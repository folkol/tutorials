# Fibonacci numbers module


def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


x = 1  # the global symbol table is only global inside this module

# statements are only executed FIRST time the module is imported (or used as main script...)
print('Initializing the module', __name__)
