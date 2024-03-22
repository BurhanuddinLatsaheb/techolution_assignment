class ValidationError(Exception):
    """
    Exception raised for validation errors.

    Attributes:
    - message (str): Explanation of the error.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)


from models import User

class UserManager:
    """
    A class for managing users.

    Attributes:
    - storage (Storage): An instance of the Storage class for data storage.
    - users (List[User]): A list of users managed by the UserManager.
    """
    def __init__(self, storage):
        """
        Initializes a UserManager object.

        Args:
        - storage (Storage): An instance of the Storage class for data storage.
        """
        self.storage = storage
        self.users = self.storage.load_users()

    def add_user(self, name, user_id):

        """
        Adds a new user to the library.

        Args:
        - name (str): The name of the user.
        - user_id (str): The ID of the user.

        Raises:
        - ValidationError: If name or user_id is empty or if a user with the same ID already exists.
        """

        if not name.strip() or not user_id.strip():
            raise ValidationError("Name and User ID are required.")
        
        if any(user.user_id == user_id.strip() for user in self.users):
            raise ValidationError("A user with the same User ID already exists.")
        
        user = User(name, user_id)
        self.users.append(user)
        self.storage.save_users(self.users)
        print(f"User '{name}' with ID '{user_id}' added successfully.")

    def update_user(self, user_id, new_name):
        """
        Updates the name of a user in the library.

        Args:
        - user_id (str): The ID of the user to update.
        - new_name (str): The new name for the user.

        Raises:
        - ValidationError: If the user is not found.
        """
        user = self.get_user_by_id(user_id)
        if user:
            user.name = new_name
            self.storage.save_users(self.users)
            print(f"User with ID '{user_id}' updated successfully. New name: '{new_name}'.")
        else:
            print(f"User with ID '{user_id}' not found.")

    def delete_user(self, user_id):
        """
        Deletes a user from the library.

        Args:
        - user_id (str): The ID of the user to delete.
        """
        user = self.get_user_by_id(user_id)
        if not user:
            print(f"User with ID '{user_id}' not found.")
            return

        if any(book.available == False for book in user.borrowed_books):
            print(f"User '{user.name}' (ID: {user_id}) has checked out books and cannot be deleted.")
            return

        self.users.remove(user)
        self.storage.save_users(self.users)
        print(f"User '{user.name}' (ID: {user_id}) deleted successfully.")

    def list_users(self):
        """
        Lists all the users in the library.
        """
        print("List of users:")
        if not self.users:
            print("No users found.")
        else:
            for user in self.users:
                print(f"- {user.name} (ID: {user.user_id})")

    def search_users(self, name=None, user_id=None):
        """
        Searches for users in the library based on name or user ID.

        Args:
        - name (str): The name to search for.
        - user_id (str): The user ID to search for.
        """
        matching_users = [user for user in self.users
                          if (not name or name.lower() in user.name.lower())
                          and (not user_id or user_id == user.user_id)]

        if not matching_users:
            print("No users found.")
        else:
            print("Matching users:")
            for user in matching_users:
                print(f"- {user.name} (ID: {user.user_id})")

    def get_user_by_id(self, user_id):
        """
        Retrieves a user from the library based on their ID.

        Args:
        - user_id (str): The ID of the user to retrieve.

        Returns:
        - User or None: The user object if found, None otherwise.
        """
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

