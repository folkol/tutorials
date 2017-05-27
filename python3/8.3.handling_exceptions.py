while False:
    try:
        x = int(input('Please enter a number: '))
        break
    except ValueError as e:
        print('Oops! That was no valid number. Try again...')

try:
    print('asd')
except (RuntimeError, TypeError, NameError) as e:
    print(e)

try:
    print('asd')
except RuntimeError as err:
    print(err)
except TypeError:
    pass
except NameError:
    pass
except:
    print('Oh snap!')
    raise
else:
    print('No exception!')

for x in range(20):
    if x == 12:
        print('Found 12!')
        break
else:
    print('No break performed')


try:
    exception = Exception('spam', 'eggs')
    raise exception
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)
    x, y = e.args
    print('x =', x)
    print('y =', y)
    print('Same instance? ', exception is e)


def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as e:
    print('Handling run-time error:', e)
