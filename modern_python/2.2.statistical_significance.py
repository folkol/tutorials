# Statistical significance of two means
# \-> shuffle slicing mean
from random import shuffle

drug = [7.1, 8.5, 6.4, 7.7, 8.2, 7.6, 8.4, 5.1, 8.1, 7.4, 6.9, 8.4]
placebo = [8.2, 6.1, 7.1, 7.1, 4.9, 7.4, 8.1, 7.1, 6.2, 7.0, 6.6, 6.3]


from statistics import mean, stdev
mean(drug)
mean(placebo)

observed_difference = mean(drug) - mean(placebo)


# Permutation test. If there is no real difference, we should be able to permute the groups without difference

combination = drug + placebo
nd = len(drug)
np = len(placebo)
shuffle(combination)


# If we we reshuffle/permute/relabel the participants
# is the new mean diff the same or more extreme than the observed?

def trial():
    shuffle(combination)
    drug = combination[:nd]
    placebo = combination[nd:]
    new_diff = mean(drug) - mean(placebo)
    return new_diff >= observed_difference

n = 100_000
p = sum(trial() for i in range(n)) / n
print(p)  # 0.061, can not reject -- need bigger sample
