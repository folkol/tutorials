with open('corpus.txt') as f:
    print(f.read())  # Read all

with open('corpus.txt') as f:
    print(f.read(10))  # Read 10, or until EOF

with open('corpus.txt') as f:
    print(f.read(-123))  # Read until EOF

with open('corpus.txt') as f:
    print(f.read())  # Read all
    print(f.read())  # Nothing
    print(f.read())  # Nothing
    print(f.read())  # Nothing

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
    print('f.tell(): ', f.tell())  # 0
    print(f.write('Hello, world!\n'))
    print('f.tell(): ', f.tell())  # 14

with open('garbage.txt', 'r+') as f:
    f.write('Hello, world!\n')
    f.seek(3)
    print(f.read())  # lo, world!

with open('garbage.txt', 'wb+') as f:
    f.write(b'DEADBEEF')
    f.seek(5)  # or f.seek(5, 0), from beginning of file
    print(f.read(1))
    f.seek(-3, 2)  # -3 from From end of file
    print(f.read(1))
    f.seek(-1, 1)  # From current position
    print(f.read(1))

f = open('corpus.txt')
f.close()
try:
    print(f.read())
except ValueError as e:
    print('Oups', e)
