def main():
    print("Passman - Password Manager".center(80, "-"))
    while choice := -1 != 0:
        print("""
        \r1. Register
        \r2. Login
        \r3. Remove User
        
        \r0. Exit""")

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
    pass


def login():
    pass


def remove():
    pass


if __name__ == '__main__':
    users: dict[str, dict:[str, str]] = {}
    main()
