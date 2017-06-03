basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # {'apple', 'pear', 'orange', 'banana'}

print('orange' in basket)  # True
print('crabgrass' in basket)  # False

a = set('abracadabra')  # set(iterable) -> new set object. {'r', 'b', 'd', 'a', 'c'}
b = set('alacazam')  # {'m', 'z', 'l', 'a', 'c'}

print(a)  # set of characters in abracadabra ({'a', 'd', 'c', 'r', 'b'})
print(b)  # set of characters in alacazam ({'z', 'a', 'm', 'l', 'c'}))
print(a - b)  # difference: in a but not in b ({'d', 'r', 'b'})
print(a | b)  # union: in a or in b ({'l', 'r', 'z', 'm', 'b', 'a', 'd', 'c'})
print(a & b)  # intersection: in a and in b ({'a', 'c'})
print(a ^ b)  # symmetric difference: a | b - a & b ({'l', 'r', 'z', 'm', 'b', 'd'})

print({c * 2 for c in 'abracadabra´' if c not in 'abc'})  # Set comprehension
