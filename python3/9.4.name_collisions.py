class Foo:
    def x(self):
        pass

    def __init__(self):
        self.x = 'x'


foo = Foo()
print(foo.x)  # x


# Function defined outside the class
def f1(self, x, y):
    print('Adding numbers for: ', self)
    return min(x, x + y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


c = C()
print(c.f(4, 5))  # 4
c.g()
c.h()


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def add_twice(self, x):
        self.add(x)
        self.add(x)


bag = Bag()

bag.add_twice(666)

print(bag.data)  # [666, 666]
