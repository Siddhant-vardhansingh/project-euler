from book import Book
class Library:

    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

b1 = Book("concepts of physics", "H.C.Verma")
b2 = Book("Electronic circuit and devices", "Robert Louise Boylestad")

L = Library()
print(L)
L.add_book(b1)
L.add_book(b2)
print(L.books)
