""" Playing the guitar with Guitar class """

from guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    # Commented out is the user input for guitars
    """name = input("Enter name of guitar: ")
    while name !="":
        year = input("Enter year: ")
        cost = input("Enter cost: ")
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)

        print("Name: {}".format(new_guitar.name))
        print("Year: {}".format(new_guitar.year))
        print("Cost: {}".format(new_guitar.cost))
        print("{} ({}) : ${} added.".format(new_guitar.name, new_guitar.year, new_guitar.cost))

        name = input("Enter name of guitar:") 
    """

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            vintage = ""
            if guitar.is_vintage():
                vintage = " (vintage)"
            print("Guitar {}: {} {}, worth ${}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage))
    else:
        name = input("Enter name of guitar:")


main()
