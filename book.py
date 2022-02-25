class Book:
    
    def __init__(self, title, author = None):
        self.title = title
        self.author = author
    def print_info(self, asked_by):
        print(self.title + " is written by " + self.author + (". And the question is asked by: ") + asked_by)
    def __repr__(self):
        return self.title


# Calling Classes

b = Book("Happy birthday")
b2 = Book("Concepts of Physics", "H.C. Verma")
print(b.title)
print(b.author)
print(b2.print_info("Siddhant"))