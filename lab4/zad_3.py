class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (
            f"Obiekt klasy Property z polami: {self.area}, "
            f"{self.rooms}, {self.price}, {self.address}"
        )


class House(Property):
    def __init__(self, plot, area, rooms, price, address):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"Obiekt klasy House z polami: {self.plot}, {self.area}, "
            f"{self.rooms}, {self.price}, {self.address}"
        )


class Flat(Property):
    def __init__(self, floor, area, rooms, price, address):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Obiekt klasy Flat z polami: {self.floor}, {self.area}, "
            f"{self.rooms}, {self.price}, {self.address}"
        )


house1 = House(2000, 300, 6, 200000, "Katowice Mikołowska")
print(house1)
flat1 = Flat(6, 50, 2, 50000, "Katowice Katowicka")
print(flat1)
