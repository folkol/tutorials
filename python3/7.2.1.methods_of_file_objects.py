with open('corpus.txt') as f:
    print(f.read())

with open('corpus.txt') as f:
    print(f.read(10))

with open('corpus.txt') as f:
    print(f.read(-123))

with open('corpus.txt') as f:
    print(f.read())
    print(f.read())
    print(f.read())
    print(f.read())

with open('corpus.txt') as f:
    print(f.readline())

with open('corpus.txt') as f:
    print(f.readline())
    print(f.readline())

with open('corpus.txt') as f:
    for line in f:
        print(line, end='')

with open('garbage.txt', 'w') as f:
    f.write('Snopp')

with open('garbage.txt', 'r+') as f:
    print(f.read())

with open('garbage.txt', 'w') as f:
    value = ('the answr', 42)
    # f.write(value)  # Argument must be a string...
    f.write(str(value))

with open('garbage.txt', 'w') as f:
    print(f.write('Hello, world!\n'))
    print(f.tell())

with open('garbage.txt', 'r+') as f:
    f.write('Hello, world!\n')
    f.seek(3)
    print(f.read())

with open('garbage.txt', 'rb+') as f:
    f.write(b'DEADBEEF')
    f.seek(5)
    print(f.read(1))
    f.seek(-3, 2)
    print(f.read(1))
    f.seek(-1, 1)
    print(f.read(1))

f = open('corpus.txt')
f.close()
try:
    print(f.read())
except ValueError as e:
    print('Oups', e)
