
class Library:
    book_list = []

    def __init__(self, book):
        self.book_taken = "Pasiekiama"
        self.book = book
        self.book_list.append(self)

    def buy_book(self):
        bought_book = Library(self)
        print(bought_book.book.book_title, bought_book.book.author.author_name, bought_book.book.author.author_surname,
              bought_book.book.book_release_date, bought_book.book_taken)
        return bought_book

    def borrow_book(self):
        self.book_taken = "Paskolinta"

    def return_book(self):
        self.book_taken = "Pasiekiama"

    class Book:
        book_list = []

        def __init__(self, book_title, book_release_date, author_name, author_surname):
            self.book_title = book_title
            self.book_release_date = book_release_date
            self.author = self.Author(author_name, author_surname)
            self.book_list.append(self)

        class Author:

            def __init__(self, author_name, author_surname):
                self.author_name = author_name
                self.author_surname = author_surname


def search_book(search, search2=""):
    if Library.book_list:
        sorted_list = []
        for book in Library.book_list:
            if book.book.book_title == search or book.book.author.author_name == search and book.book.author.author_surname == search2:
                sorted_list.append(book)

            elif book.book.book_title != search and book == Library.book_list[-1] and not sorted_list:
                print("Tokios knygos neturime")
                break

        sorted_list.sort(key=lambda x: x.book.book_release_date, reverse=True)

        for sorted_book in sorted_list:
            print(
                f"{sorted_book.book.book_title}| {sorted_book.book.author.author_name}"
                f" {sorted_book.book.author.author_surname}"
                f" | {sorted_book.book.book_release_date}m.| {sorted_book.book_taken}")

        return sorted_list
    else:
        print("Knygų šiuo metu neturime")


book1 = Library.Book("Tigras, glostantis pėdas", 2021, "Juozas", "Gaižauskas")
book2 = Library.Book("MERGINA TRAUKINY", 2018, "Paula", "Hawkins")
book3 = Library.Book("Thick as Thieves", 2019, "Sandra", "Brown")
book4 = Library.Book("DINGĘS VILNIUS", 2021, "Vladas", "Drėma")
book5 = Library.Book("Sesielis", 2021, "Vladas", "Drėma")
book6 = Library.Book("Altuorius", 5000, "Vladas", "Drėma")

buy_book = Library(book1)
buy_book2 = Library(book2)
buy_book3 = Library(book3)

while True:

    options = input("0. Sukurti knygą.\n"
                    "1. Nusipirkti naują knygos kopiją ir ją įdėti į bibliotekos kolekciją.\n"
                    "2. Pasiskolinti knygos kopiją iš bibliotekos. Leidžia pasiimti knygos kopiją, jeigu tokia yra.\n"
                    "3. Grąžinti knygos kopiją į biblioteką. Leidžia grąžinti knygos kopiją, kad ji vėl taptu 'Pasiekiama'\n"
                    "4. Rasti knygos kopiją\n"
                    "5. Išjungti programą\n")

    if options == "0":
        book_title = input("Įveskite knygos pavadinimą\n")
        author_name = input("Įveskite autoriaus vardą\n")
        author_surname = input("Įveskite autoriaus pavardę\n")
        book_release_date = int(input("Įveskite metus kada  knyga buvo publikuota\n"))
        Library.Book(book_title, book_release_date, author_name, author_surname)

    elif options == "1":
        for book in Library.Book.book_list:
            print(f"{book.book_title} | {book.author.author_name} {book.author.author_surname} | {book.book_release_date}")

        choose_book = input("Iveskite knygos pavadinimą kurią norite nusipirkti ir įdėti į biblioteką\n")

        for chosen_book in Library.Book.book_list:
            if chosen_book.book_title == choose_book:
                Library.buy_book(chosen_book)
                print("Knyga pridėta sėkmingai")
#
    elif options == "2":
        if Library.book_list:
            for book in Library.book_list:
                print(f"{book.book.book_title} | {book.book.author.author_name} {book.book.author.author_surname} |"
                      f" {book.book.book_release_date} | {book.book_taken}")

            choose_book_to_borrow = input("Iveskite knygos pavadinimą kurią norite pasiskolinti\n")

            for book in Library.book_list:
                if choose_book_to_borrow == book.book.book_title and book.book_taken == "Pasiekiama":
                    book.borrow_book()
                    break
                elif book.book.book_title != choose_book_to_borrow and book == Library.book_list[-1]:
                    print("Tokios knygos nėra, arba ivedėte blogą pavadinimą")
                    break
        else:
            print("Knygų kol kas neturime")

    elif options == "3":
        if Library.book_list:

            for book in Library.book_list:
                if book.book_taken == "Paskolinta":
                    print(book.book.book_title, book.book.author.author_name, book.book.author.author_surname,
                          book.book.book_release_date, book.book_taken)

            choose_book_to_return = input("Įveskite knygos pavadinimą kurią norite grąžinti\n")

            for book in Library.book_list:
                if book.book.book_title == choose_book_to_return and book.book_taken == "Paskolinta":
                    book.return_book()
                    print("Sėkmingai grąžinote knygą")
                    break
                elif book.book.book_title != choose_book_to_return and book == Library.book_list[-1]:
                    print("Blogai įvedėte pavadinimą arba nesate pasiskoline tokios knygos")
                    break
        else:
            print("Knygų kol kas neturime")

    elif options == "4":
        search_options = input("Pasirinkite pagal ką ieškosite:\n"
                               "1. Knygos Pavadinimą\n"
                               "2. Knygos autorių\n")
        if search_options == "1":
            search_by_title = input("Įveskite tikslų knygos pavadinimą\n")
            search_book(search_by_title)
        elif search_options == "2":
            search_by_author = input("Įveskite tikslų knygos autoriaus vardą\n")
            search_by_author2 = input("Įveskite tikslią knygos autoriaus pavardę\n")
            search_book(search_by_author, search_by_author2)

    elif options == "5":
        print("Viso gero, geros dienos!")
        quit()