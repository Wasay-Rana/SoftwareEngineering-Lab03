**Overview:**

Welcome to the Library Management System, a Python program that provides users with a convenient way to interact with a library. This system allows you to browse available books, borrow books, return books, and create user accounts. It keeps track of books, their availability, and user information.

**Features:**

1. **User Account Creation:** You can begin by creating a user account. Simply input your desired username to gain access to the library's features. This provides you with a personalized experience.

2. **Book Management:** The system allows the addition of books to the library. Each book is characterized by its title, ISBN, and availability status.

3. **Display Available Books:** Users can quickly see a list of books that are currently available in the library. This feature is handy for choosing a book to borrow.

4. **Borrowing Books:** To borrow an available book, input the title of the book you wish to borrow. The system will check its availability, mark it as borrowed, and provide you with the due date.

5. **Returning Books:** Returning a borrowed book is a straightforward process. Just enter the book's title, and the system will update its status and notify you of a successful return.

**Persistent Storage:**

For data persistence, the system utilizes a CSV (Comma-Separated Values) file to store information about books. When the program starts, it loads data from this CSV file, and when it closes, it saves any changes made. This ensures that the library's book collection remains consistent across different sessions.

**Getting Started:**

1. **Initial Setup:** Ensure that the `library_books.csv` file is located in the same directory as the Python script. This CSV file is used to store the library's book data.

2. **Running the Program:** Execute the Python script, and the system will load the book data from `library_books.csv`.

3. **User Account Creation:** If you're a new user, simply provide your username to create a user account. This account will be available throughout your session.

4. **Menu Options:**

   - **Display Available Books:** Select this option to view the list of books currently available in the library.

   - **Borrow a Book:** To borrow a book, enter the book's title. The system will check its availability and provide you with a due date for return.

   - **Return a Book:** When you return a book, input the book's title, and the system will update its status and confirm your successful return.

   - **Exit:** To conclude your session, choose the "Exit" option. The program will save any changes made to the book data to `library_books.csv`.

**Important Note:**

Please be careful with your input. The system relies on accurate book titles and availability status. Providing an invalid title or attempting to borrow an already available book will result in appropriate notifications.

**Conclusion:**

The Library Management System simplifies book management and user interaction with the library. The use of persistent storage ensures that the library's book collection remains consistent across different sessions. Enjoy exploring and utilizing the library's resources through this user-friendly interface.

**Thank you for using the Library Management System!**