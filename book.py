
from models import Book
class ValidationError(Exception):
    """
    Exception raised for validation errors.

    Attributes:
    - message (str): Explanation of the error.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class BookManager:
    """
    A class for managing books.

    Attributes:
    - storage (Storage): An instance of the Storage class for data storage.
    - books (List[Book]): A list of books managed by the BookManager.
    """
    def __init__(self , storage):
        """
        Initializes a BookManager object.

        Args:
        - storage (Storage): An instance of the Storage class for data storage.
        """
        self.storage  = storage
        self.books = self.storage.load_books()

    def add_book(self, title, author, isbn):
        """
        Adds a new book to the library.

        Args:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - isbn (str): The ISBN of the book.

        Raises:
        - ValidationError: If title, author, or ISBN is empty or if a book with the same ISBN already exists.
        """
        if not title.strip() or not author.strip() or not isbn.strip():
            raise ValidationError("Title, author, and ISBN are required.")
        
        if any(book.isbn == isbn.strip() for book in self.books):
            raise ValidationError("A book with the same ISBN already exists.")
        
        
        book = Book(title, author, isbn)
        self.books.append(book)
        self.storage.save_books(self.books)
        print(f"Book '{title}' added successfully.")

    def list_books(self):
        """
        Lists all the books in the library.
        """
        print("List of books:")
        if not self.books:
            print("No books found.")
        else:
            for book in self.books:
                print(book)

    def search_books(self, title=None, author=None, isbn=None):
        """
        Searches for books in the library based on title, author, or ISBN.

        Args:
        - title (str): The title to search for.
        - author (str): The author to search for.
        - isbn (str): The ISBN to search for.
        """
        matching_books = [book for book in self.books
                        if (not title or title.lower() in book.title.lower())
                        or (not author or author.lower() in book.author.lower())
                        or (not isbn or isbn == book.isbn)]
        if not matching_books:
            print("No books found.")
        else:
            print("Matching books:")
            for book in matching_books:
                print(book)

    def get_book_by_isbn(self, isbn):
        """
        Retrieves a book from the library based on its ISBN.

        Args:
        - isbn (str): The ISBN of the book to retrieve.

        Returns:
        - Book or None: The book object if found, None otherwise.
        """
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def delete_book(self, isbn):
        """
        Deletes a book from the library based on its ISBN.

        Args:
        - isbn (str): The ISBN of the book to delete.
        """
        book = self.get_book_by_isbn(isbn)
        if not book:
            print(f"Book with ISBN '{isbn}' not found.")
            return

        if not book.available:
            print(f"Book '{book.title}' (ISBN: {isbn}) is currently checked out and cannot be deleted.")
            return

        self.books.remove(book)
        self.storage.save_books(self.books)
        print(f"Book '{book.title}' (ISBN: {isbn}) deleted successfully.")
    
    def update_book(self, old_book, new_book):
        """
        Updates a book in the library.

        Args:
        - old_book (Book): The old book object to update.
        - new_book (Book): The new book object with updated information.

        Raises:
        - ValidationError: If the old book is not found.
        """
        if old_book in self.books:
            index = self.books.index(old_book)
            self.books[index] = new_book
            self.storage.save_books(self.books)
            print(f"Book '{old_book.title}' (ISBN: {old_book.isbn}) updated successfully.")
        else:
            print(f"Book with ISBN '{old_book.isbn}' not found.")
    