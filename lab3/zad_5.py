def isListContainNumber(list: list, number: int):
    if number in list:
        return True
    else:
        return False


print(isListContainNumber([0, 2, 4], 2))
