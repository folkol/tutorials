from typing import Dict, List


def foo(param: Dict[str, List]) -> str:
    return 'Hello, world!'


x: Dict[str, str] = dict(foo='bar', baz='qux')
print(foo(x))

