"""
Vector Object
Author: Anirudh Rowjee
Data:
    1. X, Y and Z Co-ordinates
    2. Magnitude - square root of (X^2 + Y^2 + Z^2)
    3. Normalize/Direction - Unit Vector in Direction of Vector
Operations
    1. Dot Product with Other Vector
    2. Addition with other vector
    3. Subtraction with other vectors
    4. Scalar Multiplication
    5. Scalar division
"""
import math


class Vector:
    """
    Implementation of Vector Object
    """

    def getMagnitude(self):
        """
        return the magnitude of the vector
        """
        return math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    def getDirection(self):
        """
        return the normalized / unit vector of the current vector
        """
        return list(map(lambda x: x / self.magnitude, (self.x, self.y, self.z)))

    def __init__(self, x=0.0, y=0.0, z=0.0, *args, **kwargs):
        """
        constructor method for Vector Object
        @param x: float => x co-ordinate
        @param y: float => y co-ordinate
        @param z: float => z co-ordinate
        """
        if x == None or y == None or z == None:
            raise TypeError("Inputs cannot be None.")

        self.x = x
        self.y = y
        self.z = z

        self.magnitude = self.getMagnitude()
        self.direction = self.getDirection()

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def dot(self, other):
        """
        dot product of this vector and the other one
        """
        return sum((self.x * other.x, self.y * other.y, self.z * other.z))

    def __eq__(self, other):
        """
        check for equality of two vectors
        """
        return all((self.x == other.x, self.y == other.y, self.z == other.z))

    def __add__(self, other):
        """
        scalar addition of two vectors
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """
        scalar subtraction of two vectors
        """
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        """
        scalar multiplication of a vector
        """
        if isinstance(other, (int, float)):
            # this is expected as we want to do scalar multiplication
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            # we wanted an int or a float, so we raise a TypeError
            raise TypeError("Vectors can only be multiplied with numbers")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        scalar division of a vector
        """
        if isinstance(other, (int, float)):
            # this is expected as we want to do scalar multiplication
            return Vector(self.x / other, self.y / other, self.z / other)
        else:
            # we wanted an int or a float, so we raise a TypeError
            raise TypeError("Vectors can only be multiplied with numbers")
