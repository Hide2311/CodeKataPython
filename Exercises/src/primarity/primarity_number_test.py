import pytest
import PrimarityNumber

@pytest.mark.parametrize("num", [3, 5, 0x0A, 3.2, 'a', None, True])
def test_is_prime(num):
    pn = PrimarityNumber.PrimarityNumber(num)
    assert pn.primarity_check()
