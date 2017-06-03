import fibo

print(dir(fibo))
print(help(dir))

print(dir())  # Names in current scope

print(dir(__builtins__))


# print(dir(builtins))  # NameError: name 'builtins' is not defined
import builtins
print(dir(builtins))
