class MyException(Exception):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return 'This is some exception for {} and {}.'.format(self.a, self.b)

try:
    raise MyException(123, 'poop')
except MyException as e:
    print(e.a, e.b)
    print(e)
    print(e.args)
    print(vars(e))
