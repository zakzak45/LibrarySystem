# library_system

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Registered member: {member.name}")

    def list_books(self):
        print("Library Books:")
        for book in self.books:
            print(book)

    def find_book_by_title(self, title):
        found = [book for book in self.books if title.lower() in book.title.lower()]
        if found:
            for book in found:
                print(book)
        else:
            print(f"No books found with title containing '{title}'.")


#  Example
if __name__ == "__main__":

    library = Library()


    book1 = Book("1984", "George Orwell", "9780451524935")
    book2 = Book("Python Programming", "John Zelle", "9781590282755")
    book3 = Book("The Hobbit", "J.R.R. Tolkien", "9780547928227")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

 
    member1 = Member("Alice", "M001")
    member2 = Member("Bob", "M002")

    library.register_member(member1)
    library.register_member(member2)

    member1.borrow_book(book1)     
    member2.borrow_book(book1)  
    member1.return_book(book1)  
    member2.borrow_book(book1)  


    library.list_books()

  
    library.find_book_by_title("python")
