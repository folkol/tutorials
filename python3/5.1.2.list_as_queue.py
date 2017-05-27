queue = []
queue.append(0)
queue.append(1)
queue.append(2)
queue.append(3)
queue.pop(0)  # Works, but is slow

from collections import deque
queue = deque()
queue.append(0)
queue.append(1)
queue.append(2)
queue.append(3)

print(queue.pop())
print(queue.popleft())
words = deque(['Hello', 'World', '!'])
print(words.appendleft('Wut'))
print(words.pop())
print(words.popleft())
