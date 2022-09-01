import csv
import logging


class Books():

    def __init__(self, title, author, publisher_year, publisher, url_book):

        self.title = title
        self.author = author
        self.publisher_year = publisher_year
        self.publisher = publisher
        self.url_book = url_book
        self.available = True

    def is_book_available(self):

        return self.available

    def order_book(self):

        if not self.is_book_available():
            return "%s is not available" % self.title
        self.available = False
        return "you ordered the book %s successfully" % self.title

    def return_book(self):

        self.available = True


class user():

    def __init__(self, name, email, country, address):

        self.name = name
        self.email = email
        self.country = country
        self.address = address


class library():

    def __init__(self, name, books_list, users_list):

        self.name = name
        self.books = books_list
        self.users = users_list

    def get_author(self):
        return self.name

    def add_book(self, title, author, publisher_year, publisher, url_book):
        self.books.append(Books(title, author, publisher_year, publisher, url_book))

    def add_user(self, name, email, country, address):
        self.users.append(user(name, email, country, address))

    def books_by_publish_year(self,p_year):
            return [book for book in self.books if book.publisher_year == p_year]

    def find_books_by_title(self,p_title):
        return [book for book in self.books if book.title == p_title]

    def find_book_by_author(self, p_author):
        return [book for book in self.books if book.author==p_author]

    def find_user_by_name(self,p_name):
        return [usr for usr in self.users if usr.name == p_name]

def load_users(excel_file):

    users_list = []
    try:
        with open(excel_file) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)#skip colums header
            for row in csv_reader:
                users_list.append(user(row[1], row[2], row[3], row[4]))
    except OSError:
        logging.error("Could not open " + excel_file)
        exit(1)

    return users_list

def load_books(excel_file):

    books_list = []
    try:
        with open(excel_file) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)#skip colums header
            for row in csv_reader:
                books_list.append(Books(row[1], row[2], row[3], row[4], row[5]))
    except OSError:
        logging.error("Could not open " + excel_file)
        exit(1)

    return books_list




books_objs = load_books('books_database.csv')
users_objs = load_users('users_database.csv')
library_obj = library("The Best Library", books_objs, users_objs)

book1=library_obj.find_books_by_title('A Minister   a Priest and a Rabbi')
print(book1[0].title,book1[0].author)

usr1=library_obj.find_user_by_name('Roomm')
print(usr1[0].name)