# -*- coding: utf-8 -*-

import pytest
import hanoi

@pytest.mark.parametrize("num", [1, 1000, 0x04])
def test_is_root(num):
    h = hanoi.Hanoi(num)
    assert h.start() is None
