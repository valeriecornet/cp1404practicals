"""Email storage"""

def main():
    emails_and_names = {}
    email = input("Enter email: ")
    while email != "":
        name = extract_name(email)
        name_confirmation = input("Is your name {} ? (Y/n) ".format(name))
        if name_confirmation.upper() != "Y" and name_confirmation != "":
            name = input("Enter your name:")
        emails_and_names[email] = name
        email = input("Enter email: ")

    for email in emails_and_names:
        print("{} ({})".format(emails_and_names[email], email))


def extract_name(email):
    fullname = email.split('@')[0]
    separated_name = fullname.split(".")
    print_name = " ".join(separated_name).title()
    return print_name


main()
