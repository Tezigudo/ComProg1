class Vector:
    """Define a vector in 2D space."""

    def __init__(self, x=0, y=0) -> None:
        """Initialize with x=0 and y=0 if user not input x and y"""
        self.x = x
        self.y = y

    def length(self) -> float:
        """return a length at the position using euclidean distance"""
        return (self.x ** 2 + self.y ** 2) ** .5

    def __repr__(self) -> str:
        """represent a vector"""
        return f'Vector(x={self.x}, y={self.y})'

    def dot(self, other) -> int:
        """dot vector"""
        return self.x * other.x + self.y * other.y

    def add(self, other):
        """add vector"""
        return Vector(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        """Subtract vector"""
        return Vector(self.x - other.x, self.y - other.y)

    def multiply(self, num: int):
        """multiply vector with constant magnitude num"""
        return Vector(self.x * num, self.y * num)

    def __eq__(self, other) -> bool:
        """determine if two vector are equal
        if self.x == other.x and self.y == other.y"""
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        """ help to add vector by plus sign (+)"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """ help to subtract vector by minus sign (-)"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, num: int):
        """ help to multiply vector by multiply sign (*)"""
        return Vector(self.x * num, self.y * num)

    __rmul__ = __mul__  # this help to reverse multiply (int * vector)

    @property
    def x(self) -> int:
        """ set or get value of x"""
        return self.__x

    @x.setter
    def x(self, pos):
        # check whether pos is number or not
        if not isinstance(pos, (int, float)):
            raise TypeError('The x attribute must be a number')
        self.__x = pos

    @property
    def y(self) -> int:
        """ set or get value of y"""
        return self.__y

    @y.setter
    def y(self, pos):
        # check whether pos is number or not
        if not isinstance(pos, (int, float)):
            raise TypeError('The y attribute must be a number')
        self.__y = pos


if __name__ == "__main__":
    import doctest

    doctest.testfile("docs/vector.md")
