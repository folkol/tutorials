print('Here we go')
# from foo.bar.baz import qux
print('Done')
# from foo.bar.baz import qux
print('Done?')
# print(qux)

old_locals = list(locals().keys())
from foo.bar import *
print(set(locals().keys()) - set(old_locals))


import foo
print('Foo path:', foo.__path__)
foo.__path__.append('/Users/folkol/code/python3-tutorial/foo/bar')
print('Back in packages.py')
from foo.baz import qux

print('Foo path:', foo.__path__)

print('qux:', qux)

# echo 'foo = 1' > /tmp/lollers.py
foo.__path__.append('/tmp/')

from foo.lollers import foo as fum
print('Fum?', fum)
import foo.lollers
foo.lollers.foo = 'new'
print('adas', fum)
print('adas2', foo.lollers.foo)


import sys
sys.path.append('/tmp')
import lollers  # Same file, but considered  another module
print(lollers.foo)
