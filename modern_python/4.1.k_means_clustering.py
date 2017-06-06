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
from functools import partial
from math import fsum, sqrt
from random import sample, randint
from typing import Iterable, Tuple, List, Sequence, Dict

import matplotlib.pyplot as plt


def mean(data: Iterable[float]) -> float:
    """Accurate arithmetic mean"""
    # return sum(data) / len(data)
    data = list(data)
    return fsum(data) / len(data)


Point = Tuple[int, ...]
Centroid = Point


def distance(p: Point, q: Point, fsum=fsum, sqrt=sqrt, zip=zip):  # Avoid global lookup...
    """Euclidean distance function for multi-dimensional data"""
    return sqrt(fsum((x - y) ** 2 for x, y in zip(p, q)))


def assign_data(centroids: Sequence[Centroid], points: Iterable[Point]) -> Dict[Centroid, List[Point]]:
    """Group the data points to their closest Centroid"""
    groups = defaultdict(list)
    for point in points:
        closest_centroid = min(centroids, key=partial(distance, point))
        groups[closest_centroid].append(point)
    return dict(groups)


def compute_centroids(groups: Iterable[Sequence[Point]]) -> List[Centroid]:
    """Compute the centroids for each group"""

    def transpose(data):
        """Swap the rows and columns in a 2D array of data"""
        return zip(*data)

    return [tuple(map(mean, transpose(group))) for group in groups]


def similarity(xs, ys):
    return sum(x == y for x, y in zip(xs, ys)) / len(xs)


def update_plot(labeled):
    for i, (centroid, points) in enumerate(labeled.items()):
        xs = [point[0] for point in points]
        ys = [point[1] for point in points]
        plt.scatter(xs, ys, c='bgrcmyk'[i])
    plt.pause(0.001)


def k_means(data: Iterable[Point], k: int = 2, iterations: int = 50) -> List[Centroid]:
    data = list(data)
    centroids = sample(data, k=k)  # Sample, WITHOUT replacement
    old_labels = []
    for n in range(iterations):
        labeled = assign_data(centroids, data)
        if similarity(labeled, old_labels) > 0.99:
            break
        centroids = compute_centroids(labeled.values())
        update_plot(labeled)
        old_labels = labeled
    return centroids


if __name__ == '__main__':
    plt.title('K-Means clustering (first two coordinates)')

    data = [(randint(0, 200), randint(0, 200)) for i in range(1000)]
    centroids = k_means(data, k=6)

    print('Converged!')

    xs = [centroid[0] for centroid in centroids]
    ys = [centroid[1] for centroid in centroids]
    plt.scatter(xs, ys, c='k', marker='X', s=100)
    plt.pause(0.1)
    plt.show()
