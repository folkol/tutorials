import math

print(math.cos(math.pi / 4))  # 0.7071...
print(math.log(1024, 2))  # 10.0


import random
print(random.choice(['apple', 'pear', 'banana']))  # ???

print(random.sample(range(100), 10))  # [x1, x2, x3 ... x10]
print(random.random())  # (0, 1)
print(random.randrange(6))  # [0, 6) int...


import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))  # 1.607...
print(statistics.median(data))  # 1.25
print(statistics.variance(data))  # 1.3720238095238095
