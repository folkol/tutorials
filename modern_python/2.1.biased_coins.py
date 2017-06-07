# 5 or more heads from 7 spins of a biased coin
# \-> lambda, choices, list.count

from random import choice, choices

weights = [6, 4]
cum_weights = [.6, 1]  # cumulative weights, 'when we get to tails, we have reached 100%'

choices(['heads', 'tails'], cum_weights=cum_weights)
outcome = choices(['heads', 'tails'], cum_weights=cum_weights, k=7)

print(outcome)

trial = lambda: choices(['heads', 'tails'], cum_weights=cum_weights, k=7).count('heads') >= 5
n = 10_000
print(sum(trial() for i in range(n)) / n)

# Compare to analytic approach

from math import factorial as fact

print(fact(4))


def comb(b, r):
    return fact(b) // fact(r) // fact(n - r)


print(comb(10, 3))
p_heads = 0.6

# 5 heads out of 7 spins
p_heads ** 5 * (1 - p_heads) ** 2 * comb(7, 5)

# 6 heads out of 7 spins
p_heads ** 6 * (1 - p_heads) ** 1 * comb(7, 6)

# 7 heads out of 7 spins
p_heads ** 7 * (1 - p_heads) ** 0 * comb(7, 6)

# Theoretical result, very close to empirical result.
