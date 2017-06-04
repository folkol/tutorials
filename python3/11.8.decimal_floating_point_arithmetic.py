from decimal import *

print(round(Decimal('0.70') * Decimal('1.05'), 2))  # 0.74
print(round(.70 * 1.05, 2))  # 0.73


print(sum([Decimal('0.1')]*10) == Decimal('1.0'))  # True
print(sum([0.1] * 10) == 1.0)  # False


getcontext().prec = 666
print(Decimal(1) / Decimal(7))  # 0.14285714285714285714285...
