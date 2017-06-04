from array import array

a = array('H', [4000, 10, 70, 22222])  # Homogeneus data, stored as unsigned shorts (H)
sum(a)
print(a[1:3])  # array('H', [10, 70])

from collections import deque

d = deque(['task1', 'task2', 'task3'])
d.append('task4')
print('Handling', d.popleft())  # Handling task1

starting_node = 1
unsearched = deque([starting_node])


def breadth_first_search(unsearched):
    def gen_moves(node):
        return []

    def is_goal(m):
        return False

    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
    raise ValueError('Element not found')


# print(breadth_first_search(unsearched))


import bisect

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)  # [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
print(data)  # [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]
heappush(data, -5)
print(data)  # [-5, 0, 2, 6, 1, 5, 4, 7, 8, 9, 3]
print([heappop(data) for i in range(3)])  # [-5, 0, 1]
