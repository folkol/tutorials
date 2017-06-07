import random

import matplotlib.pyplot as plt

cluster1 = [(10, 20), (120, 10), (102, 10), (12, 83), (23, 123)]
cluster2 = [(20, 20), (130, 10), (132, 10), (56, 83), (83, 123)]

data = cluster1 + cluster2

for i in range(100):
    random.shuffle(data)
    cluster1 = data[:len(cluster1)]
    cluster2 = data[len(cluster1):]
    plt.scatter([x for x, y in cluster1], [y for x, y in cluster1], c='b')
    plt.scatter([x for x, y in cluster2], [y for x, y in cluster2], c='r')
    plt.pause(0.00001)

print('Converged!')

plt.show()
