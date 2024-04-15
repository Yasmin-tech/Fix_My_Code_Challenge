#!/usr/bin/python3
"""
    a moudle that defines a square class """


class square():

    """"
        square class"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ The init function """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ The total lingth of periter """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String represntation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Creates Square object."""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
