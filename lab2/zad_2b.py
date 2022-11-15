def doubledNumber1(numbers):
    doubleNumbers = []
    for number in numbers:
        doubleNumbers.append(number * 2)
    return doubleNumbers


def doubledNumber2(numbers):
    doubledNumbers = [number * 2 for number in numbers]
    return doubledNumbers


numbers = [1, 2, 3, 4, 5]
print(doubledNumber1(numbers))
print(doubledNumber2(numbers))
