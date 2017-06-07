def fib(n):
    """Print a Fibonacci series of to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(100)
print(fib.__doc__)


def fib_list(n):
    """Returns a list containing the Fibonacci numbers up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


print(fib_list(100))


def fib(n):
    """Fibonacci generator."""
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


def fib_list(n):
    """Returns a list containing the Fibonacci numbers up to n."""
    return list(fib(n))


print(fib_list(100))

