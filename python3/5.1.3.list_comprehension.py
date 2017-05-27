x = None
print(x)

squares = []
for x in range(10):  # Will leak (and overwrite!) x...
    squares.append(x ** 2)
print(squares)

print(x)
x = None
squares = [x ** 2 for x in range(10)]  # Will not leak x
print(squares)

print(x)  # Still None

# The rightmost for iterates most frequently. Think nested for loops.
numbers = [(x, y) for x in [1, 2, 3] if x == 2 for y in [1, 2, 3] if x != y]
print(numbers)


from math import pi
pis = [str(round(pi, i)) for i in range(2, 6)]
print(pis)

print(round(123.456, -2))       # 100.0
print(str(round(123.456, -2)))  # 100.0
print(str(round(123, -2)))      # 100
print(str(round(123, -4)))      # 0
