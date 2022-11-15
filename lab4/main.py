import Classes.Zadanie1Klasy as Zadanie1
import Classes.Zadanie2Klasy as Zadanie2
import Classes.Zadanie3Klasy as Zadanie3

# Zadanie 1

student1 = Zadanie1.Student("Stefan", [100, 50, 66])
print(student1.is_passed())
student2 = Zadanie1.Student("Karolina", [10, 20, 60])
print(student2.is_passed())

# Zadanie 2

biblioteka1 = Zadanie2.Library("Katowice", "Katowicka",
                               "40-000", "8:00-18:00", "123123123")
biblioteka2 = Zadanie2.Library("Żory", "Szeroka",
                               "44-240", "10:00-20:00", "678678678")
ksiazka1 = Zadanie2.Book(biblioteka1, "20.10.2021",
                         "Jan", "Kowalski", "200")
ksiazka2 = Zadanie2.Book(biblioteka2, "21.11.2020",
                         "Henryk", "Nowak", "300")
ksiazka3 = Zadanie2.Book(biblioteka1, "02.12.2019",
                         "Małgorzata", "Kot", "100")
ksiazka4 = Zadanie2.Book(biblioteka2, "15.11.2012",
                         "Barbara", "Pies", "120")
ksiazka5 = Zadanie2.Book(biblioteka1, "12.12.1987",
                         "Wioletta", "Pomadka", "220")
pracownik1 = Zadanie2.Employee("Janusz", "Kurczak",
                               "20.02.2012", "14.06.1978", "Katowice",
                               "Mikołowska", "40-000", "000000000")
pracownik2 = Zadanie2.Employee("Janina", "Kurczak",
                               "20.02.2014", "15.07.1980", "Katowice",
                               "Mikołowska", "40-000", "000000001")
pracownik3 = Zadanie2.Employee("Mirosław", "Budyń",
                               "12.03.2010", "16.08.1985", "Katowice", "Mała",
                               "40-000", "000000002")
stud1 = Zadanie2.Stud("Anna", "Zaradna")
stud2 = Zadanie2.Stud("Marek", "Marecki")
stud3 = Zadanie2.Stud("Weronika", "Sawyer")
zamowienie1 = Zadanie2.Order(pracownik1, stud1,
                             [ksiazka1, ksiazka2], "20.09.2022")
zamowienie2 = Zadanie2.Order(pracownik3, stud3,
                             [ksiazka5, ksiazka4, ksiazka3], "18.08.2022")

print(zamowienie1)
print(zamowienie2)

# Zadanie 3

house1 = Zadanie3.House(2000, 300, 6,
                        200000, "Katowice Mikołowska")
print(house1)
flat1 = Zadanie3.Flat(6, 50, 2,
                      50000, "Katowice Katowicka")
print(flat1)
