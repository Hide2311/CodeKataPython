# -*- coding: utf-8 -*-

import pytest
import hanoi

@pytest.mark.parametrize("num", [1, "a"])
def test_is_root(num):
    h = hanoi.Hanoi(num)
    assert h.start()
