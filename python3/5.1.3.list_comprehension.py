x = None
print(x)

squares = []
for x in range(10):  # Will leak (and overwrite!) x...
    squares.append(x ** 2)
print(squares)

print(x)
x = None
double = lambda x: x * 2
squares = [double(x) for x in range(10)]  # Will not leak x
print(squares)

print(x)  # Still None

# The rightmost for iterates most frequently. Think nested for loops.
numbers = [(x, y) for x in [1, 2, 3] if x == 2 for y in [1, 2, 3] if x != y]
print(numbers)

from math import pi as π

πs = [str(round(π, i)) for i in range(2, 6)]
print(πs)

print(round(123.456, -2))  # 100.0
print(str(round(123.456, -2)))  # 100.0
print(str(round(123, -2)))  # 100
print(str(round(123, -4)))  # 0
