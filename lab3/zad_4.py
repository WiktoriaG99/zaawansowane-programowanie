def isSumGreaterThanOrEqualToThirdNumber(
    number1: int, number2: int, number3: int
) -> bool:
    if (number1 + number2) >= number3:
        return True
    else:
        return False


print(isSumGreaterThanOrEqualToThirdNumber(2, 4, 6))
