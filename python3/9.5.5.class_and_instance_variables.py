class Dog:
    kind = 'canine'

    def __init__(self, name=None):
        self.name = name


fido = Dog('Fido')
buddy = Dog('Buddy')

print(fido.kind)  # Canine, shared by all dogs
print(buddy.kind)  # Canine, shared by all dogs
print(fido.name)  # Fido
print(buddy.name)  # Buddy


class BrokenDog(Dog):
    tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


flower = BrokenDog('Flower')
star = BrokenDog('Star')

flower.add_trick('play dead')
star.add_trick('bark')

print(star.tricks)  # ['play dead', 'bark']


class GoodDog(Dog):
    def __init__(self, name):
        super().__init__(name)
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


foo = GoodDog('Foo')
bar = GoodDog('Bar')

foo.add_trick('bark')
bar.add_trick('growl')

print(foo.tricks)  # bark
print(bar.tricks)  # growl
