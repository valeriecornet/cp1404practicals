"""Check password"""

MIN_LENGTH = 6


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print(len(password) * "*")


def get_password():
    print("Password must be between 6 and 12 characters in length:")
    password = input("Enter password:")
    while len(password) < MIN_LENGTH:
        print("Invalid password")
        password = input("Enter password:")
    return password


main()
