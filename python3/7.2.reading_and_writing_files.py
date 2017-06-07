with open('corpus.txt') as f:
    print(f.readlines())

with open('corpus.txt', 'r') as f:
    print(f.readlines())

f = open('garbage.txt', 'w')
print('lol', file=f)
f.close()

with open('garbage.txt', 'w') as f:
    print('lol', file=f)

with open('garbage.txt', 'r') as f:
    print(f.read())

with open('garbage.txt', 'w') as f:
    print('lol', file=f)

with open('garbage.txt', 'a') as f:
    print('lol', file=f)

with open('garbage.txt', 'r') as f:
    print(f.read())
