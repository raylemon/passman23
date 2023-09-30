def main():
    print("Passman - Password Manager".center(80, "-"))
    while choice := -1 != 0:
        print("""
        \r1. Register
        \r2. Login
        \r3. Remove User
        
        \r0. Exit""")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                register()
            case 2:
                login()
            case 3:
                remove()
            case 0:
                exit()


def register():
    pass


def login():
    pass


def remove():
    pass


if __name__ == '__main__':
    users: dict[str, dict:[str, str]] = {}
