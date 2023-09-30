from typing import Optional


class User:
    """
    Represents a user in the system.

    Attributes:
        name (str): The username of the user.
        password (str): The password of the user.

    Methods:
        verify_password(password: str) -> bool:
            Verify if the provided password matches the stored password.

    Example:
        user = User("john_doe", "password123")
        user.verify_password("password123")  # Returns True
    """

    def __init__(self, username: str, password: str):
        """
        Initializes a User object with the given username and password.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        """
        self.name = username
        self.password = password

    def verify_password(self, password: str) -> bool:
        """
        Verify if the provided password matches the stored password.

        Args:
            password (str): The password to be verified.

        Returns:
            bool: True if the provided password matches the stored password, False otherwise.
        """
        return self.password == password

    def __str__(self) -> str:
        """
        Returns a string representation of the User object.

        Returns:
            str: The string representation of the User object.
        """
        return f"User: {self.name}"

    def __hash__(self) -> int:
        """
        Calculate the hash value of the current object.

        Returns:
            int: The hash value of the object.
        """
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        """
        Compare two User objects for equality based on their names.

        Args:
            other (User): The object to compare.

        Returns:
             bool: True if the objects are equal, False otherwise.
        """
        if isinstance(other, User):
            return self.name == other.name
        return False


class Item:
    """
    Represents an item stored in the vault.

    Attributes:
        name (str): The name of the item.
        website (str): The website associated with the item.
        login (str): The login credentials for the item.
        password (str): The password associated with the item.

    Example:
        item = Item("Email", "example.com", "john_doe", "password123")
    """

    def __init__(self, name: str, website: str, login: str, password: str):
        """
        Initializes an Item object with the given attributes.

        Args:
            name (str): The name of the item.
            website (str): The website associated with the item.
            login (str): The login credentials for the item.
            password (str): The password associated with the item.
        """
        self.name = name
        self.website = website
        self.login = login
        self.password = password

    def __str__(self) -> str:
        """
        Returns a string representation of the Item object.
        """
        return f"Item: {self.name}: {self.website}"

    def __hash__(self) -> int:
        """
        Calculate the hash value of the current object.
        """
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        """
        Compare two Item objects for equality based on their names.

        Args:
            other (Item): The object to compare.

        Returns:
             bool: True if the objects are equal, False otherwise.
        """
        if isinstance(other, Item):
            return self.name == other.name
        return False


class Vault:
    """
    Represents a vault used to store items.

    Attributes:
        items (list[Item]): The list of items stored in the vault.

    Example:
        vault = Vault()
        item = Item("Email", "example.com", "john_doe", "password123")
        vault.add_item(item)
    """

    def __init__(self):
        """
        Initializes an empty Vault object.
        """
        self.items = []

    def add_item(self, item: Item):
        """
        Adds an item to the vault.

        Args:
            item (Item): The item to be added.
        """
        if self.get_item_by_name(item.name) is not None:
            print("Item already exists")  # TODO later
            return
        else:
            self.items.append(item)

    def remove_item(self, item: Item):
        """
        Removes an item from the vault.

        Args:
            item (Item): The item to be removed.
        """
        if item not in self.items:
            print("Item not found")  # TODO later
            return
        else:
            self.items.remove(item)

    def get_items(self) -> list[Item]:
        """
        Returns the list of items stored in the vault.

        Returns:
            list[Item]: The list of items stored in the vault.
        """
        return self.items

    def get_item_by_name(self, item_name: str) -> Optional[Item]:
        """
        Returns the item with the given name from the vault.

        Args:
            item_name (str): The name of the item to be retrieved.

        Returns:
            Item: The item with the given name from the vault.
        """
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def edit_item(
        self,
        item: Item,
        new_name: str,
        new_website: str,
        new_login: str,
        new_password: str,
    ):
        """
        Edits an item in the vault with new attributes.

        Args:
            item (Item): The item to be edited.
            new_name (str): The new name of the item.
            new_website (str): The new website associated with the item.
            new_login (str): The new login credentials for the item.
            new_password (str): The new password associated with the item.

        Raises:
            ValueError: If the item is not found in the vault.
        """
        if item not in self.items:
            print("Item not found")  # TODO later
            return
        else:
            item.name = new_name
            item.website = new_website
            item.login = new_login
            item.password = new_password

    def search_by_name(self, query: str) -> list[Item]:
        return [item for item in self.items if query in item.name]
