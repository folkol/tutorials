class Foo:
    def f(self):
        pass
    print(f)  # <function f at 0x10b8270c8>


foo = Foo()

print(type(foo))  # <type 'instance'>
print(type(foo.f))  # <type 'instancemethod'>
print(type(Foo.f))  # <type 'instancemethod'>
print(foo.f is Foo.f)  # False. foo.f is a 'method object', which binds foo as self
