print('1. Entering module')

if True:  # Maybe?
    class ClassName:
        print('2. Defining class')

        def __init__(self):
            print(f'4. Defining {self}')

print('3. Going to create instance')
name = ClassName()  # Might not be defined
print(f'5. Created {name}')


class Lol:
    i = 666


l = Lol()
l2 = Lol()

l.i = 555

print(l.i)  # 555
print(l2.i)  # 666

print(Lol.i)  # 666
Lol.i = 777
print(Lol.i)  # 777
print(l.i)  # 555
print(l2.i)  # 777


class MyClass:
    print('Defining class')

    def __new__(cls, *args, **kwargs):
        print('Creating instance')
        return super().__new__(cls)  # Creates actual instance

    def __init__(self, foo, bar):  # Initializes instance, if we managed to create it
        print(foo, bar)
        self.bar = bar
        pass

    print('Defined class')


x = MyClass('foo', 'bar')  # foo bar
y = MyClass(foo='foo', bar='bar')  # foo bar
print('y.bar: ', y.bar)
z = MyClass()  # __init__() missing 2 required positional arguments: 'foo' and 'bar'
