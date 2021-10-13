"""Define Guitar class"""

class Guitar:
    """Represent a guitar object"""
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return information about guitar"""
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get age of the guitar"""
        age = 2021 - self.year
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
        