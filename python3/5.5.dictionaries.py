empty_dict = {}
d = {'foo': 1, 'bar': 'baz', 'quz': []}
print(d)

print('foo' in d)  # is key in dict. Sugar for b.__contains__(a)
del d['foo']  # Remove key from dict
print('foo' in d)  # is key in dict
d['foo'] = 1
print(d['foo'])
d['foo'] = 2
print(d['foo'])

print(list(d.keys()))
# print(d['asdf'])  # KeyError

# d[('my', ['list'])] = 'foo'  # List is not hashable, so this tuple is not hashable...


d['asdf'] = 'wut'
print(d)

for k, v in d.items():
    print(k, v)

print('for k in d.keys()')
for k in d.keys():
    print(k)

print('for k in d')  # loop over keys
for k in d:
    print(k)

print('for v in d.values()')
for v in d.values():
    print(v)


print(dict([(1, 2), ('a', 'b')]))  # dict from list of pairs
print({x: x ** x for x in range(10)})  # dict comprehension
print(dict(key1=1234, key2=122, key3='foo'))  # dict from kwargs


from collections import defaultdict


def recursive_defaultdict():
    return defaultdict(recursive_defaultdict)


dd = recursive_defaultdict()
dd['foo']['bar']['baz'] = 'qux'
print(dd)
print(dd['foo']['bar']['baz'])
print(dd.items())
