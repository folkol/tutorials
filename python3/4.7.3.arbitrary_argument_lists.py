import sys


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
    file.write("\n")
    file.flush()

write_multiple_items(sys.stdout, "^", "1", "2", "3")


def concat(*args, sep="/"):
    return sep.join(args)

print(concat("hello", "world"))
print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))
