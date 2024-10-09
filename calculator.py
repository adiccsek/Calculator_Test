def calculateSum(a, b):
    return a + b
def calculateDifference(a, b):
    return a - b
def calculateMultiply(a, b):
    return a * b
def calculateDivision(a, b):
    try:
    return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"


