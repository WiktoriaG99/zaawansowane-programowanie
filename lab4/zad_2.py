class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Obiekt klasy Library z polami: " f"{self.city}, {self.street}, itd..."


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Obiekt klasy Employee z polami: "
            f"{self.first_name}, {self.last_name}, itd..."
        )


class Stud:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Obiekt klasy Student z polami: " f"{self.name}, {self.surname}"


class Book:
    def __init__(
        self, library, publication_date, author_name, author_surname, number_of_pages
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Obiekt klasy Book z polami: "
            f"{self.library}, {self.publication_date}, itd..."
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return (
            f"Obiekt klasy Order z polami: "
            f"{self.employee}, {self.student}, {self.books}, {self.order_date}"
        )


biblioteka1 = Library("Katowice", "Katowicka", "40-000", "8:00-18:00", "123123123")
biblioteka2 = Library("Żory", "Szeroka", "44-240", "10:00-20:00", "678678678")
ksiazka1 = Book(biblioteka1, "20.10.2021", "Jan", "Kowalski", "200")
ksiazka2 = Book(biblioteka2, "21.11.2020", "Henryk", "Nowak", "300")
ksiazka3 = Book(biblioteka1, "02.12.2019", "Małgorzata", "Kot", "100")
ksiazka4 = Book(biblioteka2, "15.11.2012", "Barbara", "Pies", "120")
ksiazka5 = Book(biblioteka1, "12.12.1987", "Wioletta", "Pomadka", "220")
pracownik1 = Employee(
    "Janusz",
    "Kurczak",
    "20.02.2012",
    "14.06.1978",
    "Katowice",
    "Mikołowska",
    "40-000",
    "000000000",
)
pracownik2 = Employee(
    "Janina",
    "Kurczak",
    "20.02.2014",
    "15.07.1980",
    "Katowice",
    "Mikołowska",
    "40-000",
    "000000001",
)
pracownik3 = Employee(
    "Mirosław",
    "Budyń",
    "12.03.2010",
    "16.08.1985",
    "Katowice",
    "Mała",
    "40-000",
    "000000002",
)
stud1 = Stud("Anna", "Zaradna")
stud2 = Stud("Marek", "Marecki")
stud3 = Stud("Weronika", "Sawyer")
zamowienie1 = Order(pracownik1, stud1, [ksiazka1, ksiazka2], "20.09.2022")
zamowienie2 = Order(pracownik3, stud3, [ksiazka5, ksiazka4, ksiazka3], "18.08.2022")

print(zamowienie1)
print(zamowienie2)
