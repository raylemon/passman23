import os
import pickle

from colorama import Fore, Style, init

from src.data import Item, User, Vault


class App:
    """
    The main application class.
    """

    active_vault: Vault

    def __init__(self):
        init(autoreset=True)
        self.users: dict[User, Vault] = self.load()
        self.main()

    @staticmethod
    def load() -> dict[User, Vault]:
        """
        Loads data from a file if it exists, otherwise return an empty dictionary.

        Returns:
            dict: The loaded data if the file exists, otherwise an empty dictionary.
        """
        # TODO later
        if os.path.exists("data.dat"):
            with open("data.dat", "rb") as file:
                return pickle.load(file)
        else:
            return {}

    def save(self):
        """
        Saves data to a file.

        This function saves the data to a binary file named 'data.dat'. It uses the 'pickle' module to serialize the 'users'
        data and write it to the file

        Returns:
             None
        """
        with open("data.dat", "wb") as file:
            pickle.dump(self.users, file)

    def main(self):
        """
        The main function is the entry point of the program.
        It displays a menu to the user and executes the corresponding actions based on the user's choice.
        """
        print(Style.BRIGHT + "Passman - Password Manager".center(80, "-"))
        while (choice := -1) != 0:
            print(
                """
            \r1. Register
            \r2. Login
            \r3. Remove User
            \r4. Change password
            
            \r0. Exit"""
            )

            choice = self.ask_for_number()

            match choice:
                case 1:
                    self.register()
                case 2:
                    self.login()
                case 3:
                    self.remove_user()
                case 4:
                    self.change_password()
                case 0:
                    self.save()
                    exit()
                case _:
                    self.warning("Invalid choice")

    @staticmethod
    def ask_for_number() -> int:
        """
        Prompts the user to enter a number and returns it.

        Returns:
            int: The number entered by the user. If the input is not a valid number, returns -1.
        """

        ch = input("Enter your choice: ")
        if ch.isdigit():
            return int(ch)
        else:
            return -1

    @staticmethod
    def error(msg: str):
        """
        Print an error message.

        Args:
            msg (str): The error message to be printed.

        Returns:
            None
        """
        print(Fore.RED + Style.BRIGHT + f"Error: {msg}")

    @staticmethod
    def notice(msg: str):
        """
        Prints a notice message.

        Args:
            msg (str): The notice message to be printed.

        Returns:
            None
        """
        print(Fore.BLUE + Style.BRIGHT + f"Notice: {msg}")

    @staticmethod
    def warning(msg: str):
        """
        Print a warning message.

        Args:
            msg (str): The message to be printed.

        Returns:
            None
        """
        print(Fore.YELLOW + Style.BRIGHT + f"Warning: {msg}")

    def register(self):
        """
        Register a new user.

        This function prompts the user to enter their username. If the username
        does not already exist in the `users` dictionary, a new entry is created
        with an empty dictionary as the value. A notice is then displayed to
        indicate that the user has been successfully registered. If the username
        already exists, a warning is displayed.

        Parameters:
        None

        Returns:
        None
        """
        user_name = input("Enter your username: ")
        user_password = input("Enter your password: ")

        user = self.get_user(user_name)
        if user is not None:
            self.warning(f"{user} already exists")
        else:
            user = User(user_name, user_password)
            self.users[user] = Vault()
            self.notice(f"{user} has been registered")

    def login(self):
        """
        Logs in a user to the system.

        Parameters:
        None

        Returns:
        None
        """

        user_name = input("Enter your username: ")
        user_password = input("Enter your password: ")

        user = self.get_user(user_name)

        if user is None:
            self.error("Invalid username. Please register first.")
            return
        else:
            if user.password == user_password:
                # active_vault = users[user_name]
                self.notice(f"Logged in as {user.name}")
                self.vault_menu(user)
            else:
                self.error("Invalid password. Please try again.")

    def get_user(self, name: str) -> User | None:
        """
        Get the user object with the specified name.

        Args:
            name: The name of the user to retrieve.

        Returns:
            The user object if found, otherwise None.
        """
        # Iterate over the keys in the users dictionary
        for user in self.users.keys():
            # Check if the current user's name matches the specified name
            if user.name == name:
                # Return the user object if a match is found
                return user

        # Return None if no user with the specified name is found
        return None

    def remove_user(self):
        """
        Removes a user from the list of registered users.

        Parameters:


        Returns:
            None
        """
        user_name = input("Enter your username: ")
        user_password = input("Enter your password: ")
        user = self.get_user(user_name)

        if user is None:
            self.error("Invalid username. Please register first.")
            return
        elif user.verify_password(user_password) is False:
            self.error("Invalid password. Please try again.")
            return
        else:
            del self.users[user]
            self.notice(f"User {user_name} removed")

    def change_password(self):
        """
        Changes the password of a user.
        Returns:
            None
        """
        user_name = input("Enter your username: ")
        user_password = input("Enter your password: ")

        user = self.get_user(user_name)
        if user is None:
            self.error("Invalid username. Please register first.")
            return
        elif user.verify_password(user_password) is False:
            self.error("Invalid password. Please try again.")
            return
        else:
            user.password = input("Enter your new password: ")
            self.notice(f"Password changed")

    def vault_menu(self, user: User):
        """
        Prints the menu for the user's vault and allows them to select various actions.

        Args:
            user (User): The user object.

        Returns:
            None
        """
        print(Style.BRIGHT + f"{user}'s Vault".center(80, "-"))

        self.active_vault = self.users[user]

        while (choice := -1) != 0:
            print(
                """
            \r1. List Items
            \r2. Show item’s details
            \r3. Add item
            \r4. Edit item
            \r5. Delete item
            \r6. Search by name

            \r0. Back"""
            )

            choice = self.ask_for_number()
            match choice:
                case 1:
                    self.list_items()
                case 2:
                    self.show_item()
                case 3:
                    self.add_item()
                case 4:
                    self.edit_item()
                case 5:
                    self.delete_item()
                case 6:
                    self.search_item_by_name()
                case 0:
                    break
                case _:
                    self.warning("Invalid choice")

    def list_items(self):
        """
        Print the name and value of each item in the vault.

        Returns:
            None
        """
        [print(f"{item.name}") for item in self.active_vault.get_items()]

    def show_item(self):
        """
        Print the name, website, username, and password of the item.
        Returns:
            None
        """
        item_name = input("Enter the name of the item: ")
        item = self.active_vault.get_item_by_name(item_name)

        if item is None:
            self.error("Item not found")
        else:
            print(f"Name: {item.name}")
            print(f"Website: {item.website}")
            print(f"Username: {item.login}")
            print(f"Password: {item.password}")

    def add_item(self):
        """
        Adds an item to the vault.

        Returns:
            None
        """
        item_name = input("Enter the name of the item: ")
        item = self.active_vault.get_item_by_name(item_name)

        if item is not None:
            self.warning(f"{item} already exists")
            return
        else:
            website = input("Enter the website of the item: ")
            login = input("Enter the login of the item: ")
            password = input("Enter the password of the item: ")

            item = Item(item_name, website, login, password)
            self.active_vault.add_item(item)

    def edit_item(self):
        """
        Edit an existing item in the vault.

        Prompts the user to enter the name, website, username, and password of the item to be edited.
        If the item is not found, a warning is displayed. If the user leaves any of the fields blank,
        the old value is kept. The item is then updated with the new values.

        Returns:
            None
        """
        item_name = input("Enter the name of the item: ")
        item = self.active_vault.get_item_by_name(item_name)
        if item is None:
            self.error("Item not found")
            return

        new_name = input("Enter the new name of the item: ")
        website = input("Enter the website of the item: ")
        login = input("Enter the login of the item: ")
        password = input("Enter the password of the item: ")

        new_item = Item(
            new_name or item.name,
            website or item.website,
            login or item.login,
            password or item.password,
        )
        self.active_vault.edit_item(item, new_item)
        self.notice(f"Item {item_name} updated")

    def delete_item(self):
        """
        Deletes an item from the vault.

        Returns:
            None
        """
        item_name = input("Enter the name of the item: ")
        item = self.active_vault.get_item_by_name(item_name)
        if item is None:
            self.error("Item not found")
            return
        else:
            self.active_vault.remove_item(item)

    def search_item_by_name(self):
        """
        Perform a search by name in the vault.

        Returns:
            None
        """
        query = input("Enter search query: ")
        results = self.active_vault.search_by_name(query)

        print("\n".join(str(results)))


if __name__ == "__main__":
    app = App()
    app.main()
