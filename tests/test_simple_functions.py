import pytest
import numpy as np

from simple_functions import my_sum, factorial, my_sin


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1)
    ])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        answer = factorial(number)
        assert answer == expected

    @pytest.mark.parametrize('number, order, expected', [
        (0, 20, 0),
        (np.pi/2, 20, 1),
        (np.pi/6, 20, 1/2),
    ])
    def test_my_sin(self, number, order, expected):
        '''Test sin function'''
        answer = my_sin(number, order)
        assert np.isclose(answer, expected, atol=1e-12)
