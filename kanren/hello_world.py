from kanren import run, eq, var

x = var()
run(1, x, eq(x, 5))
