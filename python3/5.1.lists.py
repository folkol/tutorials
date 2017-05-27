xs = []

print(xs.append('Hello'))  # Add element to the end of the list
print(xs.extend(['World', '!']))  # Add all elements from the given list
print(xs.insert(0, 666))  # Insert at index. Mind the mixed types
print(xs.remove(666))  # Remove the first occurrence of this item
try:
    xs.remove('Not in list')  # Error!
except ValueError:
    pass
print(xs.pop())  # Defaults to last element...
print(xs.pop(1))  # Pop at index
del xs[0]  # Remove first element
del xs[1:200]  # Remove slice, no need to be in range
print(xs.clear())  # Removes all items. Equivalent to del a[:]
print(xs)
xs = ['Heeeeello', 'World', '!']
print(xs)
print(xs.index('!'))
print(xs.count('Hello'))
print(xs.append('Heeeeello'))
print(xs.count('Hello'))
print(xs.sort())
print(xs)
print(type(len))
print(xs.sort(key=len))  # Type warning?
print(xs)
xs.reverse()
print(xs)
print(xs is xs.copy())  # xs.copy() is equivalent to xs[:]
print(xs == xs.copy())
print(xs is xs[:])
print(xs == xs[:])
