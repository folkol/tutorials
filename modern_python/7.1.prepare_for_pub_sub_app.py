"""
Published/Subscriber Service

    Users make posts. Followers subscribe to the posts they are interested in.
    Newer posts are more releveant. Display posts by a user, or posts matching a
    search request. Display followers of a user. Display those followed by a user.
    Store the user account information with hashed passwords.

Tools we will need:
    - Unicode normalization
    - Named tuples
    - sorted(), bisect(), merge() -- reverse and key arguments
    - itertools.islice()
    - sys.intern()
    - random.expovariate()
    - time.sleep() and time.time()
    - hashlib: pbkdf2_hmac, sha256/512, digest, hexdigest
    - repr of a tuple
    - joining strings
    - floor division
    - ternary operator
    - and/or sort-circuit boolean operators that return a value
"""
from collections import namedtuple
from unicodedata import normalize, name

print('Foo Bar \u2122')
print('Foo Bar \N{TRADE MARK SIGN}')
normalize('NFC', 'foobar')  # Several normalization forms
assert normalize('NFC', '\u00f6') == normalize('NFC', '\u006f\u0308')

Person = namedtuple('Person', ['fname', 'lname', 'age'])

person = Person('Matte', 'Johansson', 36)
print(person, person.fname)

import bisect

cuts = [60, 70, 80, 90]
bisect.bisect(cuts, 67)  # index 1
grades = 'FDCBA'

grade = grades[bisect.bisect(cuts, 67)]
print(grade)

sorted([10, 5, 20])  # [5, 10, 20]
sorted([10, 5, 20] + [1, 11, 25])  # [1, 5, 10, 11, 20, 25]

a = [1, 11, 25]
b = [5, 10, 20]
c = [2, 15, 21]

sorted(a + b + c)  # Works, but might be slow
from heapq import merge

it = merge(a, b, c)
print(list(it))  # [1, 2, 5, 10, 11, 15, 20, 21, 25]

from itertools import islice

print(list(islice('abcdefghi', 3)))  # ['a', 'b', 'c']
print(list(islice('abcdefghi', None, 3)))  # ['a', 'b', 'c']
print(list(islice('abcdefghi', 2, 4)))  # ['c', 'd']
print(list(islice('abcdefghi', 0, 4, 2)))  # ['a', 'c']
it = merge(a, b, c)
print(list(islice(it, 3)))  # [1, 2, 5]

import sys

s = 'he'
t = 'llo'
u = 'hello'
v = s + t

assert u == v
assert not id(u) == id(v)

u = sys.intern(u)
v = sys.intern(v)

assert id(u) == id(v)

import random

print(random.uniform(100, 200))
print(random.triangular(100, 200))
print(random.expovariate(1 / 5))

import time

x = 10;
print(x ** 2)
# time.sleep(5); print('Done')

time.time()  # seconds since epoch (float)
time.ctime()  # Wed Jun  7 22:33:57 2017

import hashlib

# hashlib.md5('The tale of two cities')  # TypeError: Unicode-objects must be encoded before hashing
hash_object = hashlib.md5('The tale of two cities'.encode('utf-8'))  # <md5 HASH object @ 0x101501a30>
print(hash_object.digest())  # b'\x83S\xb0,<\xd3u\xba\x8d\xa2-\xdd~O"\xfa'
print(hash_object.hexdigest())  # 8353b02c3cd375ba8da22ddd7e4f22fa

print(hashlib.sha1('The tale of two cities'.encode('utf-8')).hexdigest())
print(hashlib.sha256('The tale of two cities'.encode('utf-8')).hexdigest())
print(hashlib.sha512('The tale of two cities'.encode('utf-8')).hexdigest())

h = hexdigest = hashlib.sha512('The tale of two cities'.encode('utf-8')).hexdigest()
h = hexdigest = hashlib.sha512(h.encode('utf-8')).hexdigest()
h = hexdigest = hashlib.sha512(h.encode('utf-8')).hexdigest()
h = hexdigest = hashlib.sha512(h.encode('utf-8')).hexdigest()

p = 'The tale of two cities'.encode('utf-8')
h = hashlib.pbkdf2_hmac('sha256', p, 'some phrase, or random'.encode('utf-8'), 100_000)
print(h)

s1 = 'the quick '
t1 = 'brown fox'
print(s1 + t1)

s2 = 'the quick brown '
t2 = 'fox'
print(s2 + t2)

assert s1 + t1 == s2 + t2  # Aliasing...
assert not repr((s1, t1)) == repr((s2, t2))  # Not the same
print(repr((s1, t1)))

ss = ['Raymond', 'Hettinger', 'likes', 'python']
print(' '.join(ss))  # join is the opposite to split
print(''.join(ss))

print(38 / 5)  # 7.6
print(38 // 5)  # 7

# Ternary operator, or conditional expression
score = 70
result = 'pass' if score >= 70 else 'fail'  # posres if cond else negress
print(result)

3 < 10 and 10 < 20
print(bool('hello'))  # True
'hello' and True  # 'hello'
True and 'hello'  # 'hello'
bool('')  # False
bool([])  # False
'' and 'hello'  # ''


def f(x, s=None):
    s = s or 'default'
    print(x, s)


print(f(10, 'some value'))  # 10 some value
print(f(10))  # 10 default
