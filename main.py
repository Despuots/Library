# -----------------------------------------------------------------------------------------------------------------
# 1 Užduoties nepadariau, nes man ji pasirodė kaip 0 užduotis
# Dėl unit testų man pritrūko kompetencijos
# Prašau, jeigu ir blogai padaryta užduotis palikit atsiliepima kas blogai buvo daryta, kad galėčiau tobulėti :)
# -----------------------------------------------------------------------------------------------------------------

import itertools


class Library:
    book_list = []
    id_generator = itertools.count(100)

    def __init__(self, book_title, book_author, book_release_date):
        self.title = book_title
        self.author_name = book_author
        self.book_release_date = book_release_date
        self.book_taken = "Pasiekiama"
        self.book_id = next(self.id_generator)


def display_books():
    for book in Library.book_list:
        print(f"{book.book_id}| {book.title}|{book.author_name}| {book.book_release_date}m.| {book.book_taken}")


def create_book(book_title, book_author, book_release_date):
    Library.book_list.append(Library(book_title, book_author, book_release_date))


def borrow_book(choose_book_to_borrow):
    display_books()

    if Library.book_list:
        for book in Library.book_list:
            if book.book_id == choose_book_to_borrow:
                if book.book_taken == "Paskolinta":
                    print("Knyga yra paskolinta")
                    break
                elif book.book_taken == "Pasiekiama":
                    book.book_taken = "Paskolinta"
                    print("Sekmingai pasiskolinote knyga")
                    break
            elif book.book_id != choose_book_to_borrow and book == Library.book_list[-1]:
                print("Tokios knygos nėra, arba ivedėte bloga ID")
    else:
        print("Knygu kol kas neturime")


def return_book(choose_book_to_return):
    for chosen_book in Library.book_list:
        if chosen_book.book_id == choose_book_to_return and chosen_book.book_taken == "Paskolinta":
            chosen_book.book_taken = "Pasiekiama"
            print("Sėkmingai grąžinote knygą")
            break
        elif chosen_book.book_id != choose_book_to_return and chosen_book == Library.book_list[-1]:
            print("Įvedėte blogą ID arba jūs nesate pasiskoline šios knygos")
            break


def search_book(search):
    if Library.book_list:
        sorted_list = []
        for book in Library.book_list:
            if book.title == search or book.author_name == search:
                sorted_list.append(book)
            elif book.title != search and book == Library.book_list[-1] and not sorted_list:
                print("Tokios knygos neturime")
                break

        sorted_list.sort(key=lambda x: x.book_release_date, reverse=True)

        return sorted_list
    else:
        print("Knygų šiuo metu neturime")


Library.book_list.append(Library("Tigras, glostantis pėdas", "Juozas Gaižauskas", 2021))
Library.book_list.append(Library("MERGINA TRAUKINY", "Paula Hawkins", 2018))
Library.book_list.append(Library("Thick as Thieves", "Sandra Brown", 2019))
Library.book_list.append(Library("DINGĘS VILNIUS", "Vladas Drėma", 2020))
Library.book_list.append(Library("Altuorius", "Sesielis", 5000))
Library.book_list.append(Library("Altuorius", "Sesielis", 5010))
Library.book_list.append(Library("Altuorius bruh", "Sesielis", 5000))

while True:

    options = input("0. Sukurti knygą.\n"
              "2. Pasiskolinti knygos kopiją iš bibliotekos. Leidžia pasiimti knygos kopiją, jeigu tokia yra.\n"
              "3. Grąžinti knygos kopiją į biblioteką. Leidžia grąžinti knygos kopiją, kad ji vėl taptu 'Pasiekiama'\n"
              "4. Rasti knygos kopiją\n"
              "5. Rodyti knygas\n"
              "6. Išjungti programą\n")

    if options == "0":
        book_title = input("iveskite knygos pavadinima\n")
        book_author = input("iveskite autorio varda ir pavarde\n")
        book_release_date = int(input("iveskite metus kada  knyga buvo publikuota\n"))
        create_book(book_title, book_author, book_release_date)

    elif options == "2":
        if Library.book_list:
            display_books()
            choose_book_to_borrow = int(input("Įveskite knygos ID kurią norite grąžinti\n"))
            borrow_book(choose_book_to_borrow)

    elif options == "3":
        b = 0
        for book in Library.book_list:
            if book.book_taken == "Paskolinta":
                print(book.book_id, book.title, book.author_name, book.book_release_date, book.book_taken)

        choose_book_to_return = int(input("Įveskite knygos ID kurią norite grąžinti\n"))
        return_book(choose_book_to_return)

    elif options == "4":
        search = input("Įveskite tikslų knygos pavadinimą arba autoriaus vardą ir pavardę\n")
        print("ID, Pavadinimas, Autoriaus vardas, Leidimo metai")
        for book in search_book(search):
            print(f"{book.book_id},{book.title}, {book.author_name}, {book.book_release_date}m., {book.book_taken}")

    elif options == "5":
        display_books()

    elif options == "6":
        print("Viso gero, geros dienos!")
        quit()

    else:
        print("Ivedėte bloga pasirinkimų ID")
d