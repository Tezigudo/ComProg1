from vector import Vector


class Border:
    """
    Define a border in 2D space with the lower-left corner, width, and height.
    """

    def __init__(self, corner: Vector, width: int or float, height: int or float) -> None:
        """ initialize """
        self.corner = corner
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        """ represent a Border to easily read"""
        return (f"Border(corner={self.corner},"
                f" width={self.width}, height={self.height})")

    @property
    def corner(self) -> Vector:
        """ set or get value of corner"""
        return self.__corner

    @property
    def height(self) -> int:
        """ set or get value of corner height """
        return self.__height

    @property
    def width(self) -> int:
        """ set ir get value of corner width"""
        return self.__width

    @corner.setter
    def corner(self, new_corner):
        # check whether new corner is Vector or not
        if not isinstance(new_corner, Vector):
            raise TypeError('corner must be a Vector object')
        self.__corner = new_corner

    @height.setter
    def height(self, new_height):
        # check whether new height is number or not
        if not isinstance(new_height, (int, float)):
            raise TypeError('height must be a number')
        # height cant be negative
        if new_height <= 0:
            raise ValueError('height must be greater than zero')
        self.__height = new_height

    @width.setter
    def width(self, new_width):
        # check whether new width is number or not
        if not isinstance(new_width, (int, float)):
            raise TypeError('width must be a number')
        # width cant be negative
        if new_width <= 0:
            raise ValueError('width must be greater than zero')
        self.__width = new_width

    @property
    def left(self) -> int:
        """ get value of left border"""
        return self.corner.x

    @property
    def right(self) -> int:
        """ get value of right border"""
        return self.corner.x + self.width

    @property
    def bottom(self) -> int:
        """ get value of bottom border"""
        return self.corner.y

    @property
    def top(self) -> int:
        """ get value of top border"""
        return self.corner.y + self.height

    @property
    def sides(self) -> tuple:
        """ get value of 4 side of corner / border"""
        return self.left, self.right, self.bottom, self.top

    def draw(self, painter) -> None:
        """lets draw a border"""

        painter.penup()
        painter.goto(self.left, self.bottom)
        painter.pencolor('black')
        painter.pendown()
        painter.goto(self.left, self.top)
        painter.goto(self.right, self.top)
        painter.goto(self.right, self.bottom)
        painter.goto(self.left, self.bottom)


if __name__ == "__main__":
    import doctest

    doctest.testfile('docs/border.md')
