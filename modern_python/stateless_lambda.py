x = 0


def foo():
    global x
    x += 1
    return f'8{"=" * x}o'
