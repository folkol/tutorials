from typing import Tuple, Iterable, Sequence, List, Dict, DefaultDict
from random import sample
from math import fsum, sqrt
from collections import defaultdict
# from functools import partial

def partial(func, *args):
    def inner(*moreargs):
        return func(*args, *moreargs)
    return inner

Point = Tuple[float, ...]
Centroid = Point

def mean(data: Iterable[float]) -> float:
    'Accurate arithmetic mean'
    data = list(data)
    return fsum(data) / len(data)

def dist(p: Point, q: Point, sqrt=sqrt, fsum=fsum, zip=zip) -> float:
    'Euclidean distance'
    return sqrt(fsum((x1 - x2) ** 2.0 for x1, x2 in zip(p, q)))

def assign_data(centroids: Sequence[Centroid], data: Iterable[Point]) -> Dict[Centroid, Sequence[Point]]:
    'Assign data the closest centroid'
    d : DefaultDict[Point, List[Point]] = defaultdict(list)
    for point in data:
        centroid: Point = min(centroids, key=partial(dist, point))
        d[centroid].append(point)
    return dict(d)

def compute_centroids(groups: Iterable[Sequence[Point]]) -> List[Centroid]:
    'Compute the centroid of each group'
    return [tuple(map(mean, zip(*group))) for group in groups]

def quality(labeled: Dict[Centroid, Sequence[Point]]) -> float:
    'Mean value of squared distances from data to its assigned centroid'
    return mean(dist(c, p) ** 2 for c, pts in labeled.items() for p in pts)

def k_means(data: Iterable[Point], k:int=2, iterations:int=10) -> List[Point]:
    'Return k-centroids for the data'
    data = list(data)
    centroids = sample(data, k)
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        centroids = compute_centroids(labeled.values())
    return centroids

if __name__ == '__main__':

    from pprint import pprint

    points = [
        (10, 41, 23),
        (22, 30, 29),
        (11, 42, 5),
        (20, 32, 4),
        (12, 40, 12),
        (21, 36, 23),
    ]

    centroids = k_means(points, k=2)
    pprint(assign_data(centroids, points))

if __name__ == '__main__':
    # https://www.datascience.com/blog/introduction-to-k-means-clustering-algorithm-learn-data-science-tutorials
    from pprint import pprint

    data = [

         (10, 30),
         (12, 50),
         (14, 70),

         (9, 150),
         (20, 175),
         (8, 200),
         (14, 240),

         (50, 35),
         (40, 50),
         (45, 60),
         (55, 45),

         (60, 130),
         (60, 220),
         (70, 150),
         (60, 190),
         (90, 160),
    ]

    # 5583  1338  1202  668  611  409  463
    centroids = k_means(data, k=4, iterations=20)
    d = assign_data(centroids, data)
    print(quality(d))
    pprint(d)

