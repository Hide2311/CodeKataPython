# -*- coding: utf-8 -*-

import pytest
import SquareRoot

@pytest.mark.parametrize("num", [1, 0x02, 3.0, 'a', True, None ])
def test_is_root(num):
    sr = SquareRoot.SquareRoot(num)
    assert sr.calculate_square() is None
