class BaseA:
    pass


class BaseB:
    pass


class BaseC(BaseB):
    pass


class Foo(BaseC, BaseA):
    pass


print(Foo.mro())  # Foo, BaseC, BaseB, BaseA, object

# mro: Derived classes always before their base class, left to right in declaration order


assert isinstance(1, int), '1 is instance of int'
assert isinstance(True, int), 'bool inherit from int'
assert not isinstance(1., int), 'Floats are not ints'

assert issubclass(bool, int), 'bool inherit from int'
