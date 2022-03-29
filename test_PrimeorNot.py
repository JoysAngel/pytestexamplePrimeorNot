import pytest

import PrimeorNot

@pytest.mark.parametrize("a, b", [(3, True), (4, False), (1, True), (20, False), (11, False)])
def test_prime(a,b):
    result = PrimeorNot.checkPrime(a)
    assert result == b