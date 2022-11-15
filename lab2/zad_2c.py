def showEvenNumbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)


numbers = range(10)
showEvenNumbers(numbers)
