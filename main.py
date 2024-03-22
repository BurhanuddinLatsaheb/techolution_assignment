import sys
from book import BookManager
from user import UserManager
from check import CheckManager
from models import Book, User
from storage import Storage

class LibraryManagementSystem:
    """A simple library management system."""
    def __init__(self):
        """Initialize the library management system."""
        self.storage = Storage()
        self.book_manager = BookManager(self.storage)
        self.user_manager = UserManager(self.storage)
        self.check_manager = CheckManager(self.book_manager, self.user_manager , self.storage)
        

    def display_menu(self):
        
        """
        Display the main menu options.
        """

        print("\n************** Library Management System **************")
        print("1. Book Management")
        print("2. User Management")
        print("3. Check out/in Book")
        print("4. Exit")
        print("-"*100)

    def book_management(self):
        """
            Manage books in the library.
        """
        while True:
            print("\nBook Management")
            print("1. Add Book")
            print("2. Update Book")
            print("3. Delete Book")
            print("4. List Books")
            print("5. Search Books")
            print("6. Back to Main Menu")
            print("-" * 100)
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                print("-" * 100)
                self.book_manager.add_book(title, author, isbn)
                print("-" * 100) 
            elif choice == '2':
                isbn = input("Enter the ISBN of the book to update: ")
                book = self.book_manager.get_book_by_isbn(isbn)
                if book:
                    new_title = input("Enter new book title (leave blank to keep current): ") or book.title
                    new_author = input("Enter new book author (leave blank to keep current): ") or book.author
                    new_isbn = input("Enter new book ISBN (leave blank to keep current): ") or book.isbn
                    print("-" * 100)
                    self.book_manager.update_book(book, Book(new_title, new_author, new_isbn))
                    print("-" * 100)
                else:
                    print(f"Book with ISBN '{isbn}' not found.")
            elif choice == '3':
                isbn = input("Enter the ISBN of the book to delete: ")
                book = self.book_manager.get_book_by_isbn(isbn)
                if book:
                    print("-" * 100)
                    self.book_manager.delete_book(isbn)
                    print("-" * 100)
                else:
                    print(f"Book with ISBN '{isbn}' not found.")
            elif choice == '4':
                print("-" * 100)
                self.book_manager.list_books()
                print("-" * 100)
            elif choice == '5':
                attribute = input("Enter the attribute to search (title, author, isbn): ")
                value = input(f"Enter the {attribute} to search: ")
                print("-" * 100)
                self.book_manager.search_books(attribute, value)
                print("-" * 100)
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def user_management(self):

        """
            Manage library users.
        """
        while True:
            print("\nUser Management")
            print("1. Add User")
            print("2. Update User")
            print("3. Delete User")
            print("4. List Users")
            print("5. Search Users")
            print("6. Back to Main Menu")
            print("-" * 100)

            choice = input("Enter your choice (1-6): ")
            print("-" * 100)
            if choice == '1':
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                print("-" * 100)
                self.user_manager.add_user(name, user_id)
                print("-" * 100)
            elif choice == '2':
                user_id = input("Enter the user ID of the user to update: ")
                print("-" * 100)
                user = self.user_manager.get_user_by_id(user_id)
                print("-" * 100)
                if user:
                    new_name = input("Enter new user name (leave blank to keep current): ") or user.name
                   
                    self.user_manager.update_user(user_id, new_name)
                    print("-" * 100)
                else:
                    print(f"User with ID '{user_id}' not found.")
                    print("-" * 100)
            elif choice == '3':
                user_id = input("Enter the user ID of the user to delete: ")
                print("-" * 100)
                user = self.user_manager.get_user_by_id(user_id)
                print("-" * 100)
                if user:
                    self.user_manager.delete_user(user_id)
                    print("-" * 100)
                else:
                    print(f"User with ID '{user_id}' not found.")
                    print("-" * 100)
            elif choice == '4':
                print("-" * 100)
                self.user_manager.list_users()
                print("-" * 100)
            elif choice == '5':
                print("-" * 100)
                attribute = input("Enter the attribute to search (name, user_id): ")
                value = input(f"Enter the {attribute} to search: ")
                if attribute == 'name':

                    self.user_manager.search_users(name=value)
                    print("-" * 100)
                elif attribute == 'user_id':
                    self.user_manager.search_users(user_id=value)
                    print("-" * 100)
                else:
                    print("Invalid attribute. Please try again.")
                    print("-" * 100)

            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def check_management(self):
        """
            Manage book checkouts.
        """
        while True:
            print("\nCheck out/in Book")
            print("1. Check out Book")
            print("2. Check in Book")
            print("3. List Borrowed Books")
            print("4. Back to Main Menu")
            print("-" * 100)

            choice = input("Enter your choice (1-4): ")
            print("-" * 100)
            if choice == '1':
                user_id = input("Enter your user ID: ")
                isbn = input("Enter the ISBN of the book: ")
                print("-" * 100)
                self.check_manager.checkout_book(user_id, isbn)
                print("-" * 100)
            elif choice == '2':
                user_id = input("Enter your user ID: ")
                isbn = input("Enter the ISBN of the book: ")
                print("-" * 100)
                self.check_manager.checkin_book(user_id, isbn)
                print("-" * 100)
            elif choice == '3':
                user_id = input("Enter your user ID: ")
                print("-" * 100)
                self.check_manager.list_checkouts(user_id)
                print("-" * 100)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def run(self):
        """
            Run the library management system.
        """
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.book_management()
            elif choice == '2':
                self.user_management()
            elif choice == '3':
                self.check_management()
            elif choice == '4':
                print("Exiting the Library Management System.")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    library_system.run()
