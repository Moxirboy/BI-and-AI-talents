class BookNotFoundException(Exception):
    def __init__(self, title):
        super().__init__(f"Book '{title}' not found.")

class BookAlreadyBorrowedException(Exception):
    def __init__(self, title):
        super().__init__(f"Book '{title}' is already borrowed.")

class MemberLimitExceededException(Exception):
    def __init__(self):
        super().__init__("Member has reached the maximum number of borrowed books.")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException(book_title)
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(book_title)
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise ValueError(f"Member '{member_name}' not found.")
        if len(member.borrowed_books) >= 3:
            raise MemberLimitExceededException()
        book.is_borrowed = True
        member.borrowed_books.append(book)

    def return_book(self, member_name, book_title):
        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException(book_title)
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise ValueError(f"Member '{member_name}' not found.")
        if book in member.borrowed_books:
            book.is_borrowed = False
            member.borrowed_books.remove(book)

# Testing the library system
if __name__ == "__main__":
    library = Library()

    # Adding books
    book1 = Book("1984", "George Orwell")
    book2 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")
    book4 = Book("Moby Dick", "Herman Melville")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    # Adding members
    alice = Member("Alice")
    bob = Member("Bob")
    library.add_member(alice)
    library.add_member(bob)

    # Test borrowing
    print("Alice borrows 1984:")
    library.borrow_book("Alice", "1984")
    print(f"Alice's borrowed books: {[b.title for b in alice.borrowed_books]}")

    # Test borrowing same book again
    print("\nAlice tries to borrow 1984 again:")
    try:
        library.borrow_book("Alice", "1984")
    except BookAlreadyBorrowedException as e:
        print(e)

    # Test borrowing another book
    print("\nAlice borrows The Great Gatsby:")
    library.borrow_book("Alice", "The Great Gatsby")
    print(f"Alice's books: {[b.title for b in alice.borrowed_books]}")

    # Test borrowing third book
    print("\nAlice borrows To Kill a Mockingbird:")
    library.borrow_book("Alice", "To Kill a Mockingbird")
    print(f"Alice's books: {[b.title for b in alice.borrowed_books]}")

    # Test borrowing fourth book
    print("\nAlice tries to borrow Moby Dick (should fail):")
    try:
        library.borrow_book("Alice", "Moby Dick")
    except MemberLimitExceededException as e:
        print(e)

    # Test returning a book
    print("\nAlice returns The Great Gatsby:")
    library.return_book("Alice", "The Great Gatsby")
    print(f"Alice's books after return: {[b.title for b in alice.borrowed_books]}")
    print(f"Is 'The Great Gatsby' borrowed? {book2.is_borrowed}")

    # Test borrowing a non-existent book
    print("\nBob tries to borrow 'Unknown Book':")
    try:
        library.borrow_book("Bob", "Unknown Book")
    except BookNotFoundException as e:
        print(e)
