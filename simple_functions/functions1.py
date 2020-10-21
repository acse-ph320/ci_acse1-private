from functools import lru_cache
import math

__all__ = ['my_sum', 'factorial', 'my_sin']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(n):
    return n * factorial(n-1) if n else 1


def my_sin(x, order):
    sin_x = 0

    for k in range(order):
        sin_x += (((-1)**k)/math.factorial(2*k+1))*x**(2*k+1)

    return(sin_x)
