# -*- coding: utf-8 -*-

import pytest
import leap_year

@pytest.mark.parametrize("num", [1902, 0x02, 3.0, 'a', True, None ])
def test_is_root(num):
    ly = leap_year.LeapYear(num)
    assert ly.check_leap_year()
