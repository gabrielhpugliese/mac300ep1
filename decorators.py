import time
import functools


def time_measure(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        t = time.clock()

        resp = func(*args, **kwargs)

        t = time.clock() - t
        print 'Tempo levado para conclusao do metodo: %s' % str(t)

        return resp
    return wrap

