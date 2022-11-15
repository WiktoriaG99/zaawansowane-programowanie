class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Obiekt klasy Library z polami:" \
               f" " f"{self.city}, {self.street}, itd..."


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
        return f"Obiekt klasy Student z polami: " \
               f"" f"{self.name}, {self.surname}"


class Book:
    def __init__(
        self, library, publication_date, author_name,
            author_surname, number_of_pages
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
