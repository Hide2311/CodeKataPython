import pytest
import PrimarityNumber

@pytest.mark.parametrize("num", [3, 5, 7, 11])
def test_is_prime(num):
    pn = PrimarityNumber.PrimarityNumber(num)
    assert pn.primarity_check()