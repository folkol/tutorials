print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))  # argument unpacking


def parrot(voltage, state='a stiff', action='voom'):
    print(voltage, state, action)


parrot(666)
kwargs = {
    'voltage': 666,
    'state': 'a dead',
    'action': 'barfs'
}
parrot(**kwargs)
