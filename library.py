# Simple Library Management System demonstrating OOP concepts

# Base class for all people in the library
class Person:
    # Encapsulation: name is stored inside the object
    def __init__(self, name):
        self.name = name

    # Polymorphism: This method will be overridden in child classes
    def get_role(self):
        return "Person"


# Librarian class inherits from Person
class Librarian(Person):  # Inheritance: Librarian is a type of Person
    def get_role(self):
        return "Librarian"  # Polymorphism: same method, different behavior

    # Abstraction: hides how books are added internally
    def add_book(self, library, title):
        library.books.append(Book(title))  # Adds a new Book object to the library
        print(f"'{title}' added to library.")


# Student class inherits from Person
class Student(Person):  # Inheritance: Student is a type of Person
    def get_role(self):
        return "Student"  # Polymorphism

    # Abstraction: hides borrowing logic from user
    def borrow_book(self, library, title):
        for book in library.books:
            # Encapsulation: accessing book's internal state
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                book.borrowed_by = self.name
                print(f"'{title}' borrowed by {self.name}.")
                return
        print(f"'{title}' is not available.")

    # Abstraction: hides return logic from user
    def return_book(self, library, title):
        for book in library.books:
            if book.title == title and book.borrowed_by == self.name:
                book.is_borrowed = False
                book.borrowed_by = None
                print(f" '{title}' returned by {self.name}.")
                return
        print(f" '{title}' was not borrowed by {self.name}.")


# Book class with encapsulated data
class Book:
    # Encapsulation: book status and borrower are hidden inside the class
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False
        self.borrowed_by = None


# Library class to manage books
class Library:
    def __init__(self):
        self.books = []  # Encapsulation: list of books is stored privately

    # Abstraction: shows book status without exposing internal logic
    def show_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Available" if not book.is_borrowed else f"Borrowed by {book.borrowed_by}"
            print(f" - {book.title} [{status}]")
        print()


# Testing the library system

# Create a library
library = Library()

# Create librarian and students
kenny = Librarian("Miss. Kenny")
sara = Student("Sara")
john = Student("John")

# Librarian adds books
print(f"\n{kenny.name} the {kenny.get_role()} is adding books...\n")
kenny.add_book(library, "Python Basics")
kenny.add_book(library, "Database Design 101")
print("\n")

# Students borrow and return books
print("Students are borrowing and returning books...\n")
john.borrow_book(library, "Python Basics")
sara.borrow_book(library, "Python Basics")  # Already borrowed

sara.borrow_book(library, "Database Design 101")

john.return_book(library, "Python Basics")

sara.borrow_book(library, "Python Basics")  # Now available
sara.return_book(library, "Database Design 101")  # Returning book
print("\n")

# Show current book status
library.show_books()
