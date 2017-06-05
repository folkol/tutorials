from random import sample
from statistics import median

# sample(range(100_000), 5)
# median(sample(range(100_000), 5))
# sorted(median(sample(range(100_000), 5)))
# sorted(median(sample(range(100_000), 5)))[2]

# n = 100_000
# n // 4
# n * 3 // 4


n = 100_000
trial = lambda: n // 4 < median(sample(range(n), 9)) < n * 3 // 4
p = sum(trial() for i in range(n)) / n  # Probability that the median of 5 samples falls in middle quartile

print(p)
