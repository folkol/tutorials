a, b = 0, 1             # multiple assignment
while b < 10:           # While Truthy
    print(b)
    a, b = b, a + b     # RHS is evaluated left to right
