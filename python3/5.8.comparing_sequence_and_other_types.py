# print([1, 2, 3] < (1, 2, 3))  # TypeError: unorderable types: list() < tuple()
print((1, 2,) == (1, 2))  # 'True'. Trailing comma is ignored
print([1, 2, ] < [1, 2, ])  # 'False'

print(([1, 3] < [1, 3, 1]))  # True
print(([1, 4] < [1, 3, 1]))  # False
print(([1, 4] < [1]))  # False
print(([6] < [1]))  # False
print(([] < [5]))  # True
print(([] < []))  # False
print(([1, 1, 1, 1, 3] < [1, 1, 1, 1, 2, 1, 1, 1]))  # False

print([] < [1])  # True, given equal prefix, shorter lists are considered smaller
