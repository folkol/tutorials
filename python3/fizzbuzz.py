for n in range(1, 101):
    fizz = n % 3 == 0
    buzz = n % 5 == 0

    output = ''
    if fizz and buzz:
        output = 'FizzBuzz'
    elif fizz:
        output = 'Fizz'
    elif buzz:
        output = 'Buzz'

    print(output or n)
