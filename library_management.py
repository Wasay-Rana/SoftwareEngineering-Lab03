import datetime
import csv

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return self.title

    def mark_as_unavailable(self):
        self.is_available = False

    def mark_as_available(self):
        self.is_available = True

class User:
    def __init__(self, username):
        self.username = username
        self.borrowed_books = []

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

    def search_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                return book
        return None

    def borrow_book(self, book_title, user):
        book = self.search_book(book_title)
        if book and book.is_available:
            book.mark_as_unavailable()
            user.borrowed_books.append(book)
            return book
        return None

    def return_book(self, book_title, user):
        book = self.search_book(book_title)
        if book and not book.is_available and book in user.borrowed_books:
            book.mark_as_available()
            user.borrowed_books.remove(book)
            return book
        return None

    def recommend_book(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            return available_books[0]
        else:
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

class UserLibrary:
    def __init__(self, library):
        self.library = library

# Main program
library = Library()
library.load_books_from_csv('library_books.csv')

while True:
    username = input("Enter your username (or 'exit' to quit): ")
    if username.lower() == 'exit':
        break

    user = User(username)
    print(user)

    while True:
        print("\nMenu:")
        print("1. Display Available Books")
        print("2. Search for a Book")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Recommended Book")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            book_title = input("Enter the title of the book you want to search for: ")
            book = library.search_book(book_title)
            if book:
                print(f"Book found: {book.title}")
            else:
                print("Book not found in the library.")
        elif choice == "3":
            book_title = input("Enter the title of the book you want to borrow: ")
            book = library.borrow_book(book_title, user)
            if book:
                due_date = datetime.datetime.now() + datetime.timedelta(days=14)
                print(f"You have borrowed '{book.title}'. Please return it by {due_date.strftime('%Y-%m-%d %H:%M:%S')}.")
            else:
                print("Book not available for borrowing or invalid title.")
        elif choice == "4":
            book_title = input("Enter the title of the book you want to return: ")
            book = library.return_book(book_title, user)
            if book:
                print(f"You have returned '{book.title}'.")
            else:
                print("Invalid title or book not borrowed by you.")
        elif choice == "5":
            recommended_book = library.recommend_book()
            if recommended_book:
                print(f"We recommend you to read '{recommended_book.title}'.")
            else:
                print("No recommended books available at the moment.")
        elif choice == "6":
            library.save_books_to_csv('library_books.csv')
            print("Thank you for using the library management system. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")
