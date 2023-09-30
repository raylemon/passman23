def main():
    print("Passman - Password Manager".center(80, "-"))
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
                exit()
            case _:
                warning("Invalid choice")


def ask_for_number() -> int:
    ch = input("Enter your choice: ")
    if ch.isdigit():
        return int(ch)
    else:
        return -1


def error(msg: str):
    print(f"Error: {msg}")


def notice(msg: str):
    print(f"Notice: {msg}")


def warning(msg: str):
    print(f"Warning: {msg}")


def register():
    user_name = input("Enter your username: ")
    if user_name not in users:
        users[user_name] = {}
        notice(f"Registered user: {user_name}")
    else:
        warning(f"User {user_name} already exists")


def login():
    user_name = input("Enter your username: ")
    if user_name not in users:
        error("Invalid username. Please register first.")
    else:
        global active_vault
        active_vault = users[user_name]
        notice(f"Logged in as {user_name}")
        vault_menu(user_name)


def remove():
    user_name = input("Enter your username: ")
    if user_name not in users:
        error("Invalid username. Please register first.")
    else:
        del users[user_name]
        notice(f"User {user_name} removed")


def vault_menu(user: str):
    print(f"{user}'s Vault".center(80, "-"))
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
    for name, value in active_vault.items():
        print(f"{name}: {value}")


def show_item():
    name = input("Enter item name: ")
    if name in active_vault:
        print(f"Item: {name}: {active_vault[name]}")
    else:
        warning("Item not found")


def add_item():
    name = input("Enter item name: ")
    if name not in active_vault:
        value = input("Enter item value: ")
        active_vault[name] = value
        print(f"{name}: {value} added to vault")
    else:
        warning("Item already exists")


def edit_item():
    pass


def delete_item():
    pass


def search_item():
    pass


if __name__ == "__main__":
    users: dict[str, dict:[str, str]] = {}
    active_vault: dict[str, str] = {}
    main()
