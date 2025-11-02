# Library Management System 

A Python project that demonstrates the **four core OOP concepts**:

## What This Program Does

It lets:
- A **Librarian** add books  
- **Students** borrow and return books  
- See **which books are available**

---

## The 4 OOP Concepts (Explained Simply)

| Concept           | What It Means                             | Where You See It                                        |
|-------------------|-------------------------------------------|---------------------------------------------------------|
| **Encapsulation** | Keep data safe inside an object           | `Book` hides `is_borrowed` and `borrowed_by`            |
| **Abstraction**   | Hide complex steps behind simple commands | `borrow_book()` does the hard work for you              |
| **Inheritance**   | Share common features                     | `Librarian` and `Student` both get `name` from `Person` |
| **Polymorphism**  | Same command, different result            | `.get_role()` says "Librarian" or "Student"             |

---


## Code Explained Step by Step

### 1. `Person` – The Parent Class
```python
class Person:
    def __init__(self, name):
        self.name = name
```
- Every person has a name.
- Both `Librarian` and `Student` will **inherit** this.

```python
    def get_role(self):
        return "Person"
```
- A method that says who they are.  
- Will be **changed** in child classes → **Polymorphism**

---

### 2. `Librarian` – Inherits from `Person`
```python
class Librarian(Person):
    def get_role(self):
        return "Librarian"
```
- Same method, different answer → **Polymorphism**

```python
    def add_book(self, library, title):
        library.books.append(Book(title))
```
- Adds a new book.  
- You don’t need to know *how* → **Abstraction**

---

### 3. `Student` – Also Inherits from `Person`
```python
class Student(Person):
    def get_role(self):
        return "Student"
```

#### Borrow a Book
```python
    def borrow_book(self, library, title):
        for book in library.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                book.borrowed_by = self.name
                print(f"'{title}' borrowed by {self.name}.")
                return
        print(f"'{title}' is not available.")
```
- Checks if book exists and is free  
- Updates status  
- You just call `.borrow_book()` → **Abstraction**

#### Return a Book
```python
    def return_book(self, library, title):
        # Similar logic to give book back
```
- Only the student who borrowed it can return it.

---

### 4. `Book` – Encapsulated Data
```python
class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False
        self.borrowed_by = None
```
- All book info is **bundled together** → **Encapsulation**  
- No one can mess up the data directly.

---

### 5. `Library` – Holds All Books
```python
class Library:
    def __init__(self):
        self.books = []  # Private list
```
- Only the `Library` manages the book list.

```python
    def show_books(self):
        # Prints nice list of all books and status
```
- Clean output → **Abstraction**

---

## Run the Program

Just run the file:
```bash
python library.py
```

### Sample Output
```
Miss. Kenny the Librarian is adding books...

'Python Basics' added to library.
'Database Design 101' added to library.

Students are borrowing and returning books...

'Python Basics' borrowed by John.
'Python Basics' is not available.
'Database Design 101' borrowed by Sara.
'Python Basics' returned by John.
'Python Basics' borrowed by Sara.
'Database Design 101' returned by Sara.

Library Books:
 - Python Basics [Available]
 - Database Design 101 [Available]
```

---

