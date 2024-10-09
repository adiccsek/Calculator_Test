import unittest
from calculator import calculateSum, calculateDifference, calculateMultiply, calculateDivision
    

def test_calculateSum():
    assert calculateSum(2, 3) == 5
    assert calculateSum(2, -3) == -1
    assert calculateSum(-2, -3) == -5
    assert calculateSum(0, 0) == 0

def test_calculateDifference():
    assert calculateDifference(2, 3) == -1
    assert calculateDifference(2, -3) == 5
    assert calculateDifference(-2, -3) == 1
    assert calculateDifference(0, 0) == 0

def test_calculateMultiply():
    assert calculateMultiply(2, 3) == 6
    assert calculateMultiply(2, -3) == -6
    assert calculateMultiply(-2, -3) == 6
    assert calculateMultiply(0, 0) == 0

def test_calculateDivision():
    assert calculateDivision(2, 3) == 2/3
    assert calculateDivision(2, -3) == 2/-3
    assert calculateDivision(-2, -3) == -2/-3
    try :
        calculateDivision(0, 0)
    except ZeroDivisionError:
        pass



