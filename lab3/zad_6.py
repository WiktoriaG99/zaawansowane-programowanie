def listModifications(list1: list, list2: list) -> list:
    lists = list1 + list2
    lists = set(lists)
    lists = (element**3 for element in lists)
    for element in lists:
        print(element)
    return lists


listModifications([1, 2, 3], [1, 2, 4])
