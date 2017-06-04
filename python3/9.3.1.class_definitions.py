print('1. Entering module')

if True:  # chance...
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
    def __init__(self, foo, bar):
        print(foo, bar)
        pass


x = MyClass('foo', 'bar')  # foo bar
y = MyClass(foo='foo', bar='bar')  # foo bar
