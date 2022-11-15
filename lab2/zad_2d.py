def showEverySecondNumber(numbers):
    for number in numbers:
        index = numbers[number]
        if index % 2 != 0:
            print(number)


numbers = range(10)
showEverySecondNumber(numbers)
