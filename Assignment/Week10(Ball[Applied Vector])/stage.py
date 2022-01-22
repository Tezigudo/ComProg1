import copy
from ball import Ball
from border import Border
from turtle import Turtle


class Stage:
    """
    Represent a stage for all objects such as balls and a border, as well
    as a Turtle object used to draw each object.
    """

    def __init__(self, border):
        """Initialize a stage with the given border."""

        if not isinstance(border, Border):
            raise TypeError("border must be a Border object")
        self.__border = border
        self.__balls = []

    def init_screen(self):
        """
        Prepare a display window and a turtle used to draw objects on the
        stage.
        """
        # create a turtle to be used as object painter
        self.__painter = Turtle()

        # set the turtle's display window to the size of 500x500 pixels
        self.__painter.screen.setup(500, 500)

        # do not update the turtle's drawing; we will call the
        # update method manually
        self.__painter.screen.tracer(0)

        # define the stage's coordinates so that the margins are of the size
        # 10% the width/height of the border
        self.__painter.screen.setworldcoordinates(
            self.__border.left - self.__border.width * 0.1,
            self.__border.bottom - self.__border.height * 0.1,
            self.__border.right + self.__border.width * 0.1,
            self.__border.top + self.__border.height * 0.1)

        # disable turtle's animation
        self.__painter.speed("fastest")

        # hide the turtle and initially lift the drawing pen
        self.__painter.hideturtle()
        self.__painter.penup()

    def add_ball(self, ball):
        """Add a new ball to the stage"""

        if not isinstance(ball, Ball):
            raise ValueError("Invalid object type")
        new_ball = copy.deepcopy(ball)
        new_ball.border = self.__border
        self.__balls.append(new_ball)

    def update(self, dt):
        """Update all the objects on the stage to the next time step, dt"""
        for ball in self.__balls:
            ball.update(dt)

    def render(self):
        """Render all objects on the stage on the display window"""
        self.__painter.clear()
        self.__border.draw(self.__painter)
        for ball in self.__balls:
            ball.draw(self.__painter)
        self.__painter.screen.update()
