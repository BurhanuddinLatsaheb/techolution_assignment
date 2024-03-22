class CheckManager:

    """
    A class to manage checking out and checking in books.

    Attributes:
    - book_manager (BookManager): An instance of BookManager for managing books.
    - user_manager (UserManager): An instance of UserManager for managing users.
    - storage (Storage): An instance of Storage for loading and saving checkouts data.
    - checkouts (list): A list to store tuples of checked-out books and users.
    """


    def __init__(self, book_manager, user_manager, storage):

        """
        Initializes a CheckManager instance with book_manager, user_manager, and storage.

        Args:
        - book_manager (BookManager): An instance of BookManager for managing books.
        - user_manager (UserManager): An instance of UserManager for managing users.
        - storage (Storage): An instance of Storage for loading and saving checkouts data.
        """

        self.book_manager = book_manager
        self.user_manager = user_manager
        self.storage = storage
        self.checkouts = []
        self.load_checkouts()

    def load_checkouts(self):
        """
        Loads checkouts data from storage and populates the checkouts list.
        """
        self.checkouts = self.storage.load_checkouts()

    def save_checkouts(self):
        """
        Saves checkouts data to storage.
        """
        self.storage.save_checkouts(self.checkouts)

    def checkout_book(self, user_id, isbn):
        """
        Checks out a book for a user if available.

        Args:
        - user_id (str): The ID of the user checking out the book.
        - isbn (str): The ISBN of the book to be checked out.
        """
        user = self.user_manager.get_user_by_id(user_id)
        book = self.book_manager.get_book_by_isbn(isbn)

        if user and book:
            if book.available:
                book.available = False
                user.borrowed_books.append(book)
                self.checkouts.append((user, book))
                self.save_checkouts()
                print(f"Book '{book.title}' checked out successfully by {user.name}.")
            else:
                print(f"Book '{book.title}' is not available for checkout.")
        elif not user:
            print(f"User with ID '{user_id}' not found.")
        elif not book:
            print(f"Book with ISBN '{isbn}' not found.")

    def checkin_book(self, user_id, isbn):
        """
        Checks in a book for a user if it was checked out by that user.

        Args:
        - user_id (str): The ID of the user checking in the book.
        - isbn (str): The ISBN of the book to be checked in.
        """
        user = self.user_manager.get_user_by_id(user_id)
        book = self.book_manager.get_book_by_isbn(isbn)

        if user and book:
            checkout = (user, book)
            if checkout in self.checkouts:
                self.checkouts.remove(checkout)
                book.available = True
                user.borrowed_books.remove(book)
                self.save_checkouts()
                print(f"Book '{book.title}' checked in successfully by {user.name}.")
            else:
                print(f"Book '{book.title}' is not checked out by {user.name}.")
        elif not user:
            print(f"User with ID '{user_id}' not found.")
        elif not book:
            print(f"Book with ISBN '{isbn}' not found.")

    def list_checkouts(self, user_id=None):
        """
        Lists all checkouts or checkouts for a specific user.

        Args:
        - user_id (str): The ID of the user to list checkouts for (default is None).
        """
        if user_id:
            user = self.user_manager.get_user_by_id(user_id)
            if user:
                print(f"Checkouts for {user.name}:")
                user_checkouts = [checkout for checkout in self.checkouts if checkout[0] == user]
                if not user_checkouts:
                    print("No checkouts found.")
                else:
                    for checkout in user_checkouts:
                        print(f"- {checkout[1].title} by {checkout[1].author}")
            else:
                print(f"User with ID '{user_id}' not found.")
        else:
            print("All checkouts:")
            if not self.checkouts:
                print("No checkouts found.")
            else:
                for checkout in self.checkouts:
                    print(f"- {checkout[1].title} by {checkout[1].author} (checked out by {checkout[0].name})")

    def get_user_by_id(self, user_id):
        """
        Retrieves a user by ID using the UserManager.

        Args:
        - user_id (str): The ID of the user to retrieve.

        Returns:
        - User: The User object corresponding to the user ID.
        """
        return self.user_manager.get_user_by_id(user_id)

    def get_book_by_isbn(self, isbn):
        """
        Retrieves a book by ISBN using the BookManager.

        Args:
        - isbn (str): The ISBN of the book to retrieve.

        Returns:
        - Book: The Book object corresponding to the ISBN.
        """
        return self.book_manager.get_book_by_isbn(isbn)
