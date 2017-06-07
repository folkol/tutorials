import sys


class Foo:
    def __init__(self):
        self._data = 'secret, maybe?'  # "private"


foo = Foo()

print(foo._data)  # Privacy is not enforced, though...


class Bar:
    def __f_(self):  # At least two leading underscores -> mangle name
        print('Inside __f_', type(self))
        pass

    def g(self):
        self.__f_()

    __g = g  # For reference to local class, if subclass overrides g...


bar = Bar()
bar._Bar__f_()
bar.g()

class Baz(Bar):
    pass

baz = Baz()
baz._Bar__f_()

exec('print("LOL")')
lolcode = compile('print("LOL")', 'compile_errors.log', mode='single')
print(exec(lolcode, {}))
print('666')  # Prints None

print(eval('print("LOL")'))  # Prints None
print(eval(666))  # Prints 666
