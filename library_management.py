import datetime
import csv

class Book:
    def __init__(self, title, isbn):
        self.is_available = True
        self.isbn = isbn
        self.title = title

    def __str__(self):
        return self.title

    def mark_as_unavailable(self):
        self.is_available = False

    def mark_as_available(self):
        self.is_available = True


class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"Welcome, {self.username}!"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Books available in the library:")
        for book in self.books:
            status = "Available" if book.is_available else "Not Available"
            print(f"{book.title} - {status}")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower() and book.is_available:
                book.mark_as_unavailable()
                return book
        return None

    def return_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower() and not book.is_available:
                book.mark_as_available()
                return book
        return None

    def load_books_from_csv(self, filename):
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                title, isbn, is_available = row
                book = Book(title, isbn)
                book.is_available = is_available == 'True'
                self.books.append(book)

    def save_books_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for book in self.books:
                writer.writerow([book.title, book.isbn, book.is_available])

# Main program
library = Library()
library.load_books_from_csv('library_books.csv')

user = None

while True:
    if user is None:
        username = input("Enter your username to create an account: ")
        user = User(username)
        print(user)

    print("\nMenu:")
    print("1. Display Available Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()
    elif choice == "2":
        book_title = input("Enter the title of the book you want to borrow: ")
        book = library.borrow_book(book_title)
        if book:
            due_date = datetime.datetime.now() + datetime.timedelta(days=5)
            print(f"You have borrowed '{book.title}'. Please return it by {due_date.strftime('%Y-%m-%d %H:%M:%S')}.")
        else:
            print("Book not available for borrowing or invalid title.")
    elif choice == "3":
        book_title = input("Enter the title of the book you want to return: ")
        book = library.return_book(book_title)
        if book:
            print(f"You have returned '{book.title}'.")
        else:
            print("Invalid title or book already available in the library.")
    elif choice == "4":
        library.save_books_to_csv('library_books.csv')  
        print("Jazak Allah, It was nice having you in the library management system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
