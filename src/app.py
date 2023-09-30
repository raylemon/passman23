import os
import pickle

from colorama import Fore, Style, init


def main():
    """
    The main function is the entry point of the program.
    It displays a menu to the user and executes the corresponding actions based on the user's choice.

    Parameters:


    Returns:
        None
    """

    print(Style.BRIGHT + "Passman - Password Manager".center(80, "-"))
    while (choice := -1) != 0:
        print(
            """
        \r1. Register
        \r2. Login
        \r3. Remove User
        
        \r0. Exit"""
        )

        choice = ask_for_number()

        match choice:
            case 1:
                register()
            case 2:
                login()
            case 3:
                remove()
            case 0:
                save()
                exit()
            case _:
                warning("Invalid choice")


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


def error(msg: str):
    """
    Print an error message.

    Args:
        msg (str): The error message to be printed.

    Returns:
        None
    """
    print(Fore.RED + Style.BRIGHT + f"Error: {msg}")


def notice(msg: str):
    """
    Prints a notice message.

    Args:
        msg (str): The notice message to be printed.

    Returns:
        None
    """
    print(Fore.BLUE + Style.BRIGHT + f"Notice: {msg}")


def warning(msg: str):
    """
    Print a warning message.

    Args:
        msg (str): The message to be printed.

    Returns:
        None
    """
    print(Fore.YELLOW + Style.BRIGHT + f"Warning: {msg}")


def register():
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
    if user_name not in users:
        users[user_name] = {}
        notice(f"Registered user: {user_name}")
    else:
        warning(f"User {user_name} already exists")


def login():
    """
    Logs in a user to the system.

    Parameters:
    None

    Returns:
    None
    """

    user_name = input("Enter your username: ")
    if user_name not in users:
        error("Invalid username. Please register first.")
    else:
        global active_vault
        active_vault = users[user_name]
        notice(f"Logged in as {user_name}")
        vault_menu(user_name)


def remove():
    """
    Removes a user from the list of registered users.

    Parameters:


    Returns:
        None
    """
    user_name = input("Enter your username: ")
    if user_name not in users:
        error("Invalid username. Please register first.")
    else:
        del users[user_name]
        notice(f"User {user_name} removed")


def vault_menu(user: str):
    """
    Prints the menu for the user's vault and allows them to select various actions.

    Args:
        user (str): The name of the user.

    Returns:
        None
    """
    print(Style.BRIGHT + f"{user}'s Vault".center(80, "-"))
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

        choice = ask_for_number()
        match choice:
            case 1:
                list_items()
            case 2:
                show_item()
            case 3:
                add_item()
            case 4:
                edit_item()
            case 5:
                delete_item()
            case 6:
                search_item()
            case 0:
                break
            case _:
                warning("Invalid choice")


def list_items():
    """
    Print the name and value of each item in the active_vault dictionary.

    Parameters:
    None

    Returns:
    None
    """
    for name, value in active_vault.items():
        print(f"{name}: {value}")


def show_item():
    """
    Show an item from the active vault based on the user's input.

    Parameters:


    Returns:
        None
    """
    name = input("Enter item name: ")
    if name in active_vault:
        print(f"Item: {name}: {active_vault[name]}")
    else:
        warning("Item not found")


def add_item():
    """
    Adds an item to the active vault.

    Parameters:


    Returns:
        None
    """
    name = input("Enter item name: ")
    if name not in active_vault:
        value = input("Enter item value: ")
        active_vault[name] = value
        print(f"{name}: {value} added to vault")
    else:
        warning("Item already exists")


def edit_item():
    """
    Edit an item in the active vault.

    Prompts the user to enter the name of the item to be edited. If the item
    is found in the active vault, the user is prompted to enter a new name
    and value for the item. If the user leaves either field blank, the old
    name or value is kept. The item is then updated in the active vault.

    Parameters:
    None

    Returns:
    None
    """
    name = input("Enter item name: ")
    if name in active_vault:
        (input("Enter item new name or leave blank to keep old name: ") or name)
        new_value = (
            input("Enter item value or leave blank to keep old value: ")
            or active_vault[name]
        )

        del active_vault[name]
        active_vault[name] = new_value
        notice(f"Item {name} updated")
    else:
        warning("Item not found")


def delete_item():
    """
    Deletes an item from the active vault.

    Parameters:


    Returns:
        None

    Description:
        This function prompts the user to enter the name of an item to delete from the active vault. If the item is
        found in the active vault, it is deleted and a notice is displayed. Otherwise, a warning is displayed indicating
        that the item was not found.
    """
    name = input("Enter item")
    if name in active_vault:
        del active_vault[name]
        notice("Item removed")
    else:
        warning("Item not found")


def search_item():
    """
    Perform a search for an item in the active_vault based on a user-provided query.

    Parameters:
    None

    Returns:
    None
    """
    query = input("Enter search query: ")
    for name, value in active_vault.items():
        if query in name or query in value:
            print(f"{name}: {value}")


def load():
    """
    Load data from a file if it exists, otherwise return an empty dictionary.

    Returns:
        dict: The loaded data if the file exists, otherwise an empty dictionary.
    """
    if os.path.exists("data.dat"):
        with open("data.dat", "rb") as file:
            return pickle.load(file)
    else:
        return {}


def save():
    """
    Save the data to a file.

    This function saves the data to a binary file named 'data.dat'. It uses the 'pickle' module to serialize the 'users'
    data and write it to the file.

    Parameters:


    Returns:
        None
    """
    with open("data.dat", "wb") as file:
        pickle.dump(users, file)


if __name__ == "__main__":
    init(autoreset=True)
    users: dict[str, dict:[str, str]] = load()
    active_vault: dict[str, str] = {}
    main()
