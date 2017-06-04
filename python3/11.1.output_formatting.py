import reprlib

chars = set('supercalifragilisticexpialidocious')
print(chars)  # {'p', 'd', 'x', 'l', 'e', 'g', 't', 'c', 's', 'u', 'f', 'i', 'o', 'r', 'a'}
print(reprlib.repr(chars))  # {'a', 'c', 'd', 'e', 'f', 'g', ...}

import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]

pprint.pprint(t, width=30)

"""
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
"""

import textwrap

doc = """The wrap() method is just like fill() except that it returns
 a list of strings instead of one big string with newlines to separate
 the wrapped lines."""

xs = textwrap.fill(doc, width=40)
assert type(xs) == str
print(xs)
"""
The wrap() method is just like fill()
except that it returns  a list of
strings instead of one big string with
newlines to separate  the wrapped lines.
"""

ys = textwrap.wrap(doc, width=40)
assert type(ys) == list

pprint.pprint(ys)
"""
['The wrap() method is just like fill()',
 'except that it returns  a list of',
 'strings instead of one big string with',
 'newlines to separate  the wrapped lines.']
 """


import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
conv = locale.localeconv()
x = 1234567.8
print(locale.format('%f', x, grouping=True))  # 1,234,567.800000
print(locale.format('%d', x, grouping=True))  # 1,234,567
print(locale.format('%d', x, grouping=False))  # 1234567

s = locale.format_string('%s%.*f', (conv['currency_symbol'], conv['frac_digits'], x), grouping=True)
print(s)  # $1,234,567.80
