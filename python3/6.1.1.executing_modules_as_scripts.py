from fibo import fib


if __name__ == '__main__':
    import sys
    for i in sys.argv[1:]:
        fib(int(i))
