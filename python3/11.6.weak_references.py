import weakref, gc


class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


a = A(10)

wa = weakref.ref(a)
print('Weakref count:', weakref.getweakrefcount(a))  # 1
print(wa())  # 10
del a
print(wa())  # None

a = A(10)


def on_delete(x):
    print('Deleted:', x)  # weakref, real object gone by now


wa = weakref.ref(a)
wa2 = weakref.ref(a, on_delete)

print('Weakref count:', weakref.getweakrefcount(a))  # 2
del a
gc.collect()


a = A(10)

d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])  # 10
print('Weakref count:', weakref.getweakrefcount(a))  # 1
del a
gc.collect()
# print(d['primary'])  # KeyError: 'primary'
