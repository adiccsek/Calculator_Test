import pytest
from calculator import calculateSum, calculateDifference, calculateMultiply, calculateDivision

def test_calculateSum():
    assert calculateSum(2, 3) == 5
    assert calculateSum(2, -3) == -1
    assert calculateSum(-2, -3) == -5
    assert calculateSum(0, 0) == 0