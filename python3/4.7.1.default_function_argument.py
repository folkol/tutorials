def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)


# ask_ok('wut')
# ask_ok('wut', 2)
# ask_ok('wut', 2, 'rumpa')

i = [5]


def f(arg=i):
    print(arg)
    arg.append(2)


i = 6
f()  # prints [5]
f()  # prints [5, 2]...
f()
f()


def g(n=1, acc=[]):
    acc.append(n)
    print(acc)


g()
g()
g()
g()
g()
