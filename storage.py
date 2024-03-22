import json
from models import Book, User

class Storage:
    """
        A class to manage loading and saving data for books, users, and checkouts.

        Attributes:
        - books_file_path (str): The file path for storing books data.
        - users_file_path (str): The file path for storing users data.
        - checkouts_file_path (str): The file path for storing checkouts data.
    """
    def __init__(self, books_file_path="books.json", users_file_path="users.json", checkouts_file_path="checkouts.json"):
        
        """
            Initializes a Storage instance with file paths for books, users, and checkouts.

            Args:
            - books_file_path (str): The file path for storing books data.
            - users_file_path (str): The file path for storing users data.
            - checkouts_file_path (str): The file path for storing checkouts data.
        """
        
        self.books_file_path = books_file_path
        self.users_file_path = users_file_path
        self.checkouts_file_path = checkouts_file_path

    def load_books(self):


        """
            Loads books data from the specified file path.

            Returns:
            - list: A list of Book objects loaded from the file.
        """
        
        try:
            with open(self.books_file_path, "r") as file:
                books_data = json.load(file)
            books = [self._convert_book_data(book_data) for book_data in books_data]
            return books
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON data in {self.books_file_path}")
            return []

    def save_books(self, books):
        """
        Saves books data to the specified file path.

        Args:
        - books (list): A list of Book objects to be saved.
        """


        books_data = [self._convert_book_object(book) for book in books]
        try:
            with open(self.books_file_path, "w") as file:
                json.dump(books_data, file, indent=4)
        except IOError:
            print(f"Error: Unable to write to {self.books_file_path}")

    def load_users(self):
        """
        Loads users data from the specified file path.

        Returns:
        - list: A list of User objects loaded from the file.
        """

        try:
            with open(self.users_file_path, "r") as file:
                users_data = json.load(file)
            users = [self._convert_user_data(user_data) for user_data in users_data]
            return users
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON data in {self.users_file_path}")
            return []

    def save_users(self, users):

        """
        Saves users data to the specified file path.

        Args:
        - users (list): A list of User objects to be saved.
        """

        users_data = [self._convert_user_object(user) for user in users]
        try:
            with open(self.users_file_path, "w") as file:
                json.dump(users_data, file, indent=4)
        except IOError:
            print(f"Error: Unable to write to {self.users_file_path}")

    def load_checkouts(self):
        """
        Loads checkouts data from the specified file path.

        Returns:
        - list: A list of tuples containing User and Book objects loaded from the file.
        """

        try:
            with open(self.checkouts_file_path, "r") as file:
                checkouts_data = json.load(file)
            checkouts = [(self._convert_user_data(checkout[0]), self._convert_book_data(checkout[1])) for checkout in checkouts_data]
            return checkouts
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON data in {self.checkouts_file_path}")
            return []

    def save_checkouts(self, checkouts):
        """
        Saves checkouts data to the specified file path.

        Args:
        - checkouts (list): A list of tuples containing User and Book objects to be saved.
        """


        checkouts_data = [(self._convert_user_object(checkout[0]), self._convert_book_object(checkout[1])) for checkout in checkouts]
        try:
            with open(self.checkouts_file_path, "w") as file:
                json.dump(checkouts_data, file, indent=4)
        except IOError:
            print(f"Error: Unable to write to {self.checkouts_file_path}")

    @staticmethod
    def _convert_book_data(book_data):

        """
        Converts book data from a dictionary to a Book object.

        Args:
        - book_data (dict): A dictionary containing book data.

        Returns:
        - Book: A Book object created from the book data.
        """

        return Book(**book_data)

    @staticmethod
    def _convert_book_object(book):

        """
        Converts a Book object to a dictionary.

        Args:
        - book (Book): The Book object to be converted.

        Returns:
        - dict: A dictionary containing the book data.
        """

        return {
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "available": book.available
        }

    @staticmethod
    def _convert_user_data(user_data):

        """
        Converts user data from a dictionary to a User object.

        Args:
        - user_data (dict): A dictionary containing user data.

        Returns:
        - User: A User object created from the user data.
        """

        borrowed_books_data = user_data.pop('borrowed_books', [])
        borrowed_books = [Book(**book_data) for book_data in borrowed_books_data]
        user_data['borrowed_books'] = borrowed_books
        return User(**user_data)

    @staticmethod
    def _convert_user_object(user):

        """
        Converts a User object to a dictionary.

        Args:
        - user (User): The User object to be converted.

        Returns:
        - dict: A dictionary containing the user data.
        """

        borrowed_books_data = [book.__dict__ for book in user.borrowed_books]
        user_data = user.__dict__.copy()
        user_data['borrowed_books'] = borrowed_books_data
        return user_data


