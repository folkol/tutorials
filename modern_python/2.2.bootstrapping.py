# Bootstrapping is used when re-sampling is hard or expensive
from random import choices

timings = [7.18, 8.59, 12.24, 7.39, 8.16, 8.68, 6.98, 8.31, 9.06, 7.06, 7.67, 10.02, 6.87, 9.07]

from statistics import mean, stdev

mean(timings)
stdev(timings)


# Build a 90% confidence interval

def bootstrap(data):
    """Resampling the same sample"""
    return choices(data, k=len(data))


n = 10_000
means = sorted([mean(bootstrap(timings)) for i in range(n)])

print(f'The observed mean of {mean(timings)}')
print(f'Falls in a 90% confidence interval from {means[500] :.1f} to {means[-500] :.1f}')
