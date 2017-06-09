"""Simple message publisher/subscriber service

Users make posts. Followers subscribe to the posts they are interested in.
Newer posts are more relevant. Display posts by a user, posts for a user, or
posts matching a search request. Display followers or a user. Display those
followed by a user. Store the user account information with hashed passwords."""

import time
from collections import defaultdict, deque
from heapq import merge
from itertools import islice
from typing import NamedTuple, DefaultDict, Set, List, Optional

User = str
Post = NamedTuple('Post', [('timestamp', float), ('user', str), ('text', str)])

posts: deque = deque()
user_posts: DefaultDict[User, deque] = defaultdict(deque)
following: DefaultDict[User, Set[User]] = defaultdict(set)
followers: DefaultDict[User, Set[User]] = defaultdict(set)


def post_message(user: User, text: str, timestamp: float = None) -> None:
    timestamp = timestamp or time.time()
    post = Post(timestamp=timestamp, user=user, text=text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)


def follow(user: User, followed_user: User) -> None:
    following[user].add(followed_user)
    followers[followed_user].add(user)


def posts_by_user(user: User, limit: Optional[int]=None) -> List[Post]:
    return list(islice(user_posts[user], limit))


def posts_for_user(user: User, limit: Optional[int]=None) -> List[Post]:
    posts = merge(*[user_posts[followee] for followee in following[user]], reverse=True)
    return list(islice(posts, limit))

def search(phrase: str, limit: Optional[int]=None) -> List[Post]:
    # TODO: Add indexing?
    # TODO: Add caching?
    return list(islice((post for post in posts if phrase in post.text), limit))
