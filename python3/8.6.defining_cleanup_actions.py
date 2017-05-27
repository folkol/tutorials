# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero')
    else:
        print('The result is', result)
    finally:
        print('Executing finally clause')


divide(2, 1)
divide(2, 0)

divide("2", "1")
