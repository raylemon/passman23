import os
import pickle

from colorama import Fore, Style, init

from src.data import User, Vault


#
#

#
#
# def vault_menu(user: str, active_vault: dict[str, str]):
#     """
#     Prints the menu for the user's vault and allows them to select various actions.
#
#     Args:
#         user (str): The name of the user.
#         active_vault (dict[str, str]): The dictionary containing the items to search through.
#
#
#     Returns:
#         None
#     """
#     print(Style.BRIGHT + f"{user}'s Vault".center(80, "-"))
#     while (choice := -1) != 0:
#         print(
#             """
#         \r1. List Items
#         \r2. Show item’s details
#         \r3. Add item
#         \r4. Edit item
#         \r5. Delete item
#         \r6. Search by name
#
#         \r0. Back"""
#         )
#
#         choice = ask_for_number()
#         match choice:
#             case 1:
#                 list_items(active_vault)
#             case 2:
#                 show_item(active_vault)
#             case 3:
#                 add_item(active_vault)
#             case 4:
#                 edit_item(active_vault)
#             case 5:
#                 delete_item(active_vault)
#             case 6:
#                 search_item(active_vault)
#             case 0:
#                 break
#             case _:
#                 warning("Invalid choice")
#
#
# def list_items(active_vault: dict[str, str]):
#     """
#     Print the name and value of each item in the active_vault dictionary.
#
#     Parameters:
#     active_vault (dict[str, str]): The dictionary containing the items to search through.
#
#
#     Returns:
#     None
#     """
#     [print(f"{name}: {value}") for name, value in active_vault.items()]
#
#
# def show_item(active_vault: dict[str, str]):
#     """
#     Show an item from the active vault based on the user's input.
#
#     Parameters:
#     active_vault (dict[str, str]): The dictionary containing the items to search through.
#
#
#     Returns:
#         None
#     """
#     name = input("Enter item name: ")
#     if name in active_vault:
#         print(f"Item: {name}: {active_vault[name]}")
#     else:
#         warning("Item not found")
#
#
# def add_item(active_vault: dict[str, str]):
#     """
#     Adds an item to the active vault.
#
#     Parameters:
#     active_vault (dict[str, str]): The dictionary containing the items to search through.
#
#
#     Returns:
#         None
#     """
#     name = input("Enter item name: ")
#     if name not in active_vault:
#         value = input("Enter item value: ")
#         active_vault[name] = value
#         print(f"{name}: {value} added to vault")
#     else:
#         warning("Item already exists")
#
#
# def edit_item(active_vault: dict[str, str]):
#     """
#     Edit an item in the active vault.
#
#     Prompts the user to enter the name of the item to be edited. If the item
#     is found in the active vault, the user is prompted to enter a new name
#     and value for the item. If the user leaves either field blank, the old
#     name or value is kept. The item is then updated in the active vault.
#
#     Parameters:
#     active_vault (dict[str, str]): The dictionary containing the items to search through.
#
#     Returns:
#     None
#     """
#     name = input("Enter item name: ")
#     if name in active_vault:
#         new_name = input("Enter item new name or leave blank to keep old name: ")
#         new_value = input("Enter item value or leave blank to keep old value: ")
#
#         active_vault[name] = new_value if new_value else active_vault[name]
#         active_vault[new_name] = active_vault.pop(name)
#
#         notice(f"Item {name} updated")
#     else:
#         warning("Item not found")
#
#
# def delete_item(active_vault: dict[str, str]):
#     """
#     Deletes an item from the active vault.
#
#     Parameters:
#     active_vault (dict[str, str]): The dictionary containing the items to search through.
#
#
#     Returns:
#         None
#
#     Description:
#         This function prompts the user to enter the name of an item to delete from the active vault. If the item is
#         found in the active vault, it is deleted and a notice is displayed. Otherwise, a warning is displayed indicating
#         that the item was not found.
#     """
#     name = input("Enter item")
#     if name in active_vault:
#         del active_vault[name]
#         notice("Item removed")
#     else:
#         warning("Item not found")
#
#
# def search_item(active_vault: dict[str, str]):
#     """
#     Perform a search for an item in the active_vault based on a user-provided query.
#
#     Parameters:
#     active_vault (dict[str, str]): The dictionary containing the items to search through.
#
#     Returns:
#     None
#     """
#     query = input("Enter search query: ")
#     results = [
#         f"{name}: {value}"
#         for name, value in active_vault.items()
#         if query in name or query in value
#     ]
#     print("\n".join(results))
#


class App:
    """
    The main application class.
    """

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
        pass


if __name__ == "__main__":
    app = App()
    app.main()
