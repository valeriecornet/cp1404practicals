"""Testing guitar class methods and printing"""

from guitar import Guitar


def test():
    """Test methods for Gibson and another guitar"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print("{} get_age() - Expected 99. Got {}".format(gibson.name, gibson.get_age()))

    another_guitar = Guitar("Another Guitar", 2013, 9000.00)
    print("{} get_age() - Expected 8. Got {}".format(another_guitar.name, another_guitar.get_age()))

    print("{} is_vintage() - Expected True. Got {}".format(gibson.name, gibson.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name,another_guitar.is_vintage()))


test()
