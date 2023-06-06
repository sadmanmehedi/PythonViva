class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def size_book(self):
        return self.no_of_books

a=Library()
a.add_book("Harry_Potter")
a.add_book("The Alchemist")
a.add_book("FIFA BOOK")

print(a.size_book())
