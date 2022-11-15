def isNumberEven(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


result = isNumberEven(2)

if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
