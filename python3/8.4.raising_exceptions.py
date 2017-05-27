try:
    raise NameError('Hithere')
except NameError as e:
    print('Got:', e)

try:
    raise NameError
except NameError as e:
    print('Got:', e)

try:
    raise BaseException
except BaseException as e:
    print('Got:', e)

try:
    raise None
except Exception as e:
    print('Got:', type(e), e)
