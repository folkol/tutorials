def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(123)
parrot(123, type='penis')


def cheeseshop(kind, *args, **kwargs):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in args:
        print(arg)
    print("-" * 40)
    keys = sorted(kwargs.keys())
    for kw in keys:
        print(kw, ":", kwargs[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
