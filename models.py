from dataclasses import dataclass, field
from typing import List



@dataclass
class Book:

    """
    A class representing a book.

    Attributes:
    - title (str): The title of the book.
    - author (str): The author of the book.
    - isbn (str): The ISBN of the book.
    - available (bool): Whether the book is available or not (default is True).
    """

    title: str
    author: str
    isbn: str
    available: bool = True

    def to_dict(self):
        """
        Converts the book object to a dictionary.

        Returns:
        - dict: A dictionary representation of the book object.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        """
        Creates a book object from a dictionary.

        Args:
        - data (dict): A dictionary containing book data.

        Returns:
        - Book: A Book object created from the dictionary data.
        """
        return Book(data["title"], data["author"], data["isbn"], data["available"])


    def check_out(self):
        """
        Checks out the book if it is available.
        """
        if self.available:
            self.available = False
            print(f"Book '{self.title}' checked out successfully.")
        else:
            print(f"Book '{self.title}' is not available for checkout.")

    def check_in(self):
        """
            Checks in the book if it is not already available.
        """
        if not self.available:
            self.available = True
            print(f"Book '{self.title}' checked in successfully.")
        else:
            print(f"Book '{self.title}' is already available.")

    def update(self, title=None, author=None, isbn=None):
        """
        Updates the book's title, author, or ISBN if provided.

        Args:
        - title (str): The new title for the book.
        - author (str): The new author for the book.
        - isbn (str): The new ISBN for the book.
        """
        if title:
            self.title = title
        if author:
            self.author = author
        if isbn:
            self.isbn = isbn
        print(f"Book '{self.title}' updated successfully.")

@dataclass
class User:
    """
    A class representing a user.

    Attributes:
    - name (str): The name of the user.
    - user_id (str): The ID of the user.
    - borrowed_books (List[Book]): A list of books borrowed by the user (default is an empty list).
    """
    name: str
    user_id: str
    borrowed_books: List[Book] = field(default_factory=list)

    def borrow_book(self, book):
        """
        Allows the user to borrow a book if it is available.

        Args:
        - book (Book): The book to be borrowed.
        """
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"Book '{book.title}' borrowed successfully by {self.name}.")
        else:
            print(f"Book '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        """
        Allows the user to return a borrowed book.

        Args:
        - book (Book): The book to be returned.
        """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"Book '{book.title}' returned successfully by {self.name}.")
        else:
            print(f"Book '{book.title}' is not borrowed by {self.name}.")

    def list_borrowed_books(self):
        """
        Lists all books borrowed by the user.
        """
        print(f"Borrowed books by {self.name}:")
        if not self.borrowed_books:
            print("No books borrowed.")
        else:
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author} (ISBN: {book.isbn})")