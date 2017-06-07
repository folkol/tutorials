"""Use K-means to locate voting clusters in the U.S. Congress

    Data set:   Senate voting record on 28 passed bills for the 2016 (114th) Congress
    Source:     https://www.govtrack.us/congress
"""

import csv
from collections import namedtuple, defaultdict, Counter
from glob import glob as expand_filename
from typing import DefaultDict, List, Dict, Tuple

import matplotlib.pyplot as plt

from k_means import k_means, assign_data

NUM_SENATORS = 100

Senator = namedtuple('Senator', ['name', 'party', 'state'])
VoteValue = int
VoteHistory = Tuple[VoteValue, ...]

vote_value: Dict[str, VoteValue] = {
    'Nay': -1,
    'Not Voting': 0,
    'Yea': 1
}

# Load votes which were arranged by topic, and accumulate votes by senator
vote_accumulator: DefaultDict[Senator, List[VoteValue]] = defaultdict(list)
for filename in expand_filename('rhettiger/congress_data/*.csv'):
    with open(filename) as f:
        reader = csv.reader(f)
        vote_topic = next(reader)
        headers = next(reader)
        for person, state, district, vote, name, party in reader:
            senator = Senator(name, party, state)
            vote_accumulator[senator].append(vote_value[vote])

votes = {senator: tuple(votes) for senator, votes in vote_accumulator.items()}

# Use k-means to locate the cluster centroids from pattern of votes,
# assign each senator to the nearest cluster
centroids = k_means(votes.values(), k=3)
clustered_votes = assign_data(centroids, votes.values())

votes_to_senators = defaultdict(list)
for senator, vote_history in votes.items():
    votes_to_senators[vote_history].append(senator)
assert sum(len(cluster) for cluster in votes_to_senators.values()) == NUM_SENATORS

# Display the clusters and the members (senators) of each cluster
for i, cluster in enumerate(clustered_votes.values(), start=1):
    print(f'================ Voting Cluster ${i} ================ ')
    party_totals = Counter()
    for votes in cluster:
        for senator in votes_to_senators[votes]:
            party_totals[senator.party] += 1
            print(senator)
    print(party_totals)
