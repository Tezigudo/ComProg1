from border import Border
from copy import copy, deepcopy
from vector import Vector


class Ball:
    """
    Maintains ball objects which can calculate their own movements.
    """

    def __init__(self, pos: Vector, vel: Vector, acc: Vector) -> None:
        """ Initailize a class """

        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.border = None
        self.color = 'black'
        # tracking whick index-1 is head else tail
        self.track = [(copy(self.pos.x), copy(self.pos.y)) for _ in range(11)]

    def __repr__(self) -> str:
        """Represent a class with a ball self and parameter"""
        return f'Ball(pos={self.pos}, vel={self.vel}, acc={self.acc})'

    @property
    def pos(self) -> Vector:
        """ get or set value of ball's position"""
        return self.__pos

    @pos.setter
    def pos(self, new_pos: Vector):
        # check if new pos is vector object or not
        if not isinstance(new_pos, Vector):
            raise TypeError('pos must be a Vector object')
        self.__pos = deepcopy(new_pos)

    @property
    def vel(self) -> Vector:
        """ get or set value of ball's velocity"""
        return self.__vel

    @vel.setter
    def vel(self, new_vel: Vector):
        # check if new vel is vector object or not
        if not isinstance(new_vel, Vector):
            raise TypeError('vel must be a Vector object')
        self.__vel = deepcopy(new_vel)

    @property
    def acc(self) -> Vector:
        """ get or set value of ball's acceleration"""
        return self.__acc

    @acc.setter
    def acc(self, new_acc: Vector):
        # check if new acc is vector object or not
        if not isinstance(new_acc, Vector):
            raise TypeError('acc must be a Vector object')
        self.__acc = deepcopy(new_acc)

    def valid_border(self) -> bool:
        """
        check if valid border
        """
        left, right, bottom, top = self.border.sides
        valid_x = left <= self.pos.x <= right
        valid_y = bottom <= self.pos.y <= top
        return valid_x and valid_y

    @property
    def border(self) -> Border:
        """ get or set value of ball border"""
        return self.__border

    @border.setter
    def border(self, other: Border):
        # check whether border is instance of Border or None
        if not isinstance(other, (Border, type(None))):
            raise TypeError('border must be a Border object')
        self.__border = deepcopy(other)
        # check if border is not valid
        if self.__border and not self.valid_border():
            raise ValueError("border must cover the current ball's position")

    @property
    def color(self) -> str:
        """ get or set value of ball's color"""
        return self.__color

    @color.setter
    def color(self, other: str):
        # check whetehr color is string
        if not isinstance(other, str):
            raise TypeError('color must be a string')
        self.__color = deepcopy(other)

    def update(self, time: float) -> None:
        """
        Update a velocity and position if it hit corder it will update more

        and update the ball tracking
        """
        self.vel = self.vel.add(self.acc.multiply(time))
        self.pos = self.pos.add(self.vel.multiply(time))

        if self.border:  # check if it have border and update velocity and position
            # check if position over bottom
            if self.pos.y <= self.border.bottom:
                self.pos.y = 2 * self.border.bottom - self.pos.y
                self.vel.y *= -1
            # check if position over top
            if self.pos.y >= self.border.top:
                self.pos.y = 2 * self.border.top - self.pos.y
                self.vel.y *= -1
            # check if position over right
            if self.pos.x >= self.border.right:
                self.pos.x = 2 * self.border.right - self.pos.x
                self.vel.x *= -1
            # check if position over left
            if self.pos.x <= self.border.left:
                self.pos.x = 2 * self.border.left - self.pos.x
                self.vel.x *= -1
        # append new head and put other to tail
        self.track.append((self.pos.x, self.pos.y))
        self.track = self.track[1:]

    def draw(self, painter) -> None:
        """ draw the ball on 1 frame"""

        painter.penup()
        # draw a tail
        painter.pencolor(self.color)
        painter.goto(*self.track[0])  # goto last position of tail
        painter.pendown()
        for tail_pos in self.track[:-1]:
            # each iterate will draw the ball from tail to headposition
            painter.goto(*tail_pos)
        painter.goto(*self.track[-1])  # goto head position
        painter.dot(10, self.color)  # draw a head


if __name__ == "__main__":
    import doctest

    doctest.testfile("docs/ball.md")
