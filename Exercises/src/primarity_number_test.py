import pytest
import 03_PrimarityNumber

@pytest.mark.parametrize("num", [3, 4, 5])
def test_is_prime(num):
    pn = PrimarityNumber(count)
    assert pn.primarity_check()
    
