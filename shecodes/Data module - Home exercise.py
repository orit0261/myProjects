from pprint import pprint

books = [
        ('Title:Harry Potter', 'Author:J. K. Rolling', 'Genre:Fantasy'),
        ('Title:Anna Karenina', 'Author:Leo Tolstoy', 'Genre:Novel'),
        ('Title:Lolita', 'Author:Vladimir Nabokov', 'Genre:Novel'),
        ('Title:Hamlet', 'Author:William Shakespeare', 'Genre:Tragedy, Drama'),
        ('Title:Crime and Punishment', 'Author:Fyodor Dostoyevsky', 'Genre:Novel, Fiction, Crime Fiction'),
        ('Title:Emma', 'Author:Jane Austen', 'Genre:Novel'),
        ('Title:Mrs. Dalloway', 'Author:Virginia Woolf', 'Genre:Novel'),
        ('Title:To Kill a Mockingbird', 'Author:Harper Lee', 'Genre:Novel, Tragedy'),
        ('Title:The Stranger', 'Author:Albert Camus', 'Genre:Crime Fiction, Novel'),
        ('Title:Rabbit, Run', 'Author:John Updike', 'Genre:Novel')
         ]


def get_list_of_books(books_input):
    new_list = []
    for book in books_input:
        book_dict = {}
        title, author, genre = book
        book_dict['Title'] = title.split(':')[1]
        book_dict['Author'] = author.split(':')[1]
        book_dict['Genre'] = genre.split(':')[1]
        book_dict['Availability'] = True
        new_list.append(book_dict)
    return new_list


def book_gen():
    books_dicts = get_list_of_books(books)
    for bookDict in books_dicts:
        if bookDict['Availability']:
            yield bookDict


library_books = get_list_of_books(books)


def is_book_available(book_title):
    for book in library_books:
        if book['Title'] == book_title:
            if book['Availability']:
                return True
            break
    return False


pprint(get_list_of_books(books))
gen = book_gen()
pprint(gen)
pprint(next(gen))