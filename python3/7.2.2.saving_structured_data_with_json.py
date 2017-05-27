import json

data = [1, 'simple', 'list']
print(type(json.dumps(data)))
print(repr(json.dumps(data)))
print(json.dumps(data))

with open('garbage.txt', 'w') as f:
    json.dump(data, f)

with open('garbage.txt') as f:
    x = json.load(f)

assert data == x, 'Unexpected obj: {}'.format(x)


# See also: pickle module for arbitrary serialization...
