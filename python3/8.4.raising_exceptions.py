try:
    raise NameError('Hi there')
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

try:
    raise BaseException
except BaseException as e:
    try:
        try:
            try:
                raise BaseException('foo1')
            except BaseException as a:
                raise BaseException('bar1') from a  # Not needed, implicit chain
        except BaseException as e:
            raise
    except BaseException as e:
        print('Gottt:', e)
        print('Gotttr:', e.__cause__)

try:
    raise BaseException
except BaseException as e:
    try:
        try:
            raise BaseException('foo2')
        except BaseException as a:
            raise BaseException('bar2') from None  # Suppress chain
    except BaseException as e:
        raise
