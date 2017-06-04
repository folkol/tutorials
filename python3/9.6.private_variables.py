class Foo:
    def __init__(self):
        self._data = 'secret, maybe?'  # "private"

foo = Foo()

print(foo._data)  # Privacy is not enforced, though...
