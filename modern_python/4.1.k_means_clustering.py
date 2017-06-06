"""Cluster Analysis, preparations

Big Idea:
    K-means is an unsupervised learning tool for identifying clusters within datasets.

Algorithm in English:
    Pick arbitrary points as guesses for the center of each group.
    Assign all the data points to the closest matching group.
    Within each group, average the points to get a new guess for the center of the group.
    Repeat multiple times: assign the data and averag the points

Goal:
    Express the idea more clearly and beautifully in Python than in English.


Topics to prepare for Resampling:
    - Type hinting
    - fsum, true division
    - defaultdict grouping
    - key functions
    - zip(*)
    - flattening with nested for-loop
    - list(iterator)

Functions needed for Kmean:
    - mean(data)
    - dist(point, point)
    - assign_data(centroids, points)
    - compute_centroids(groups)
    - k_means(points

"""
from collections import defaultdict
from pprint import pprint
from random import sample, randint
from typing import Iterable, Tuple, List, Sequence, Dict
import matplotlib.pyplot as plt

points = [
    (10, 41, 23),
    (22, 30, 29),
    (11, 42, 5),
    (20, 32, 4),
    (12, 40, 12),
    (21, 36, 23)
]

# from statistics import mean  # Accurate arithmetic mean
from math import fsum, sqrt


def mean(data: Iterable[float]) -> float:
    """Accurate arithmetic mean"""
    # return sum(data) / len(data)
    data = list(data)
    return fsum(data) / len(data)


# from math import hypot  # Distance in 2D

Point = Tuple[int, ...]
Centroid = Point


def distance(p: Point, q: Point, fsum=fsum, sqrt=sqrt, zip=zip):  # Avoid global lookup...
    """Euclidean distance function for multi-dimensional data"""
    return sqrt(fsum((x - y) ** 2 for x, y in zip(p, q)))


from functools import partial


def assign_data(centroids: Sequence[Centroid], points: Iterable[Point]) -> Dict[Centroid, List[Point]]:
    """Group the data points to their closest Centroid"""
    groups = defaultdict(list)
    for point in points:
        # closest_centroid = min(centroids, key=lambda centroid: distance(centroid, point))
        closest_centroid = min(centroids, key=partial(distance, point))
        groups[closest_centroid].append(point)
    return dict(groups)


centroids = [(10, 41, 23), (12, 40, 12)]
"""
defaultdict(<class 'list'>,
            {(10, 41, 23): [(10, 41, 23),
                            (22, 30, 29),
                            (21, 36, 23)],
             (12, 40, 12): [(11, 42, 5),
                            (20, 32, 4),
                            (12, 40, 12)]})
"""
groups = [
    [(10, 41, 23), (22, 30, 29), (21, 36, 23)],
    [(11, 42, 5), (20, 32, 4), (12, 40, 12)]
]


# [17.666666666666668, 35.666666666666664, 25.0]
# pprint(list(map(mean, zip(*group))))


def compute_centroids(groups: Iterable[Sequence[Point]]) -> List[Centroid]:
    """Compute the centroids for each group"""
    def transpose(data):
        """Swap the rows and columns in a 2D array of data"""
        return zip(*data)
    return [tuple(map(mean, transpose(group))) for group in groups]


def k_means(data: Iterable[Point], k: int = 2, iterations: int = 50) -> List[Centroid]:
    data = list(data)
    centroids = sample(data, k=k)  # Sample -> WITHOUT replacement
    for i in range(iterations):  # We might write some code for detecting oscillations or convergence
        labeled = assign_data(centroids, data)
        for i, (centroid, points) in enumerate(labeled.items()):
            plt.scatter([x for x, y in points], [y for x, y in points], c='br'[i])
            plt.pause(0.05)
        centroids = compute_centroids(labeled.values())
    return centroids


if __name__ == '__main__':
    # points = [
    #     (10, 41, 23),
    #     (22, 30, 29),
    #     (11, 42, 5),
    #     (20, 32, 4),
    #     (12, 40, 12),
    #     (21, 36, 23)
    # ]
    points = [(randint(0, 200), randint(0, 200)) for i in range(500)]
    k_means(points)

    print('Convered!')

    plt.show()
