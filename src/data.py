class User:
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
