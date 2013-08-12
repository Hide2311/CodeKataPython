import pytest
import prime_number

@pytest.mark.parametrize("num", [3, 5, 0x0A, 3.2, 'a', None, True])
def test_is_prime(num):
    pn = prime_number.PrimNumber(num)
    assert pn.primarity_check()
