try:
    10 * (1 / 0)
except ZeroDivisionError as zde:
    print(zde)

try:
    1 + spam * 3
except NameError as ne:
    print(ne)

try:
    '2' + 2
except TypeError as e:
    print(e)
