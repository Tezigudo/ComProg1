# Module `border.py`

The module `border.py` defines the `Border` class.  Each `Border` object consists of
the `corner`, `width`, and `height` properties.  The `corner` property must be a
`Vector` object, where the `width` and `height` are positive numbers.

    >>> from border import Border
    >>> from vector import Vector

    >>> type(Border.corner)
    <class 'property'>
    >>> type(Border.width)
    <class 'property'>
    >>> type(Border.height)
    <class 'property'>


Initialization
==============

A `Border` object must be initialized with a corner, a width, and a height.

    >>> border = Border(Vector(3, 4), 5, 6)
    >>> border
    Border(corner=Vector(x=3, y=4), width=5, height=6)


Updating Properties
===================

The `corner` property can only be assigned with a `Vector` object.

    >>> border.corner = Vector(6, 7)
    >>> border.corner
    Vector(x=6, y=7)
    >>> border.corner = "hello"
    Traceback (most recent call last):
    ...
    TypeError: corner must be a Vector object

The `width` and `height` properties must be numbers (either `int` or `float`) <u>greater than zero</u>.

    >>> border.width = 3.1
    >>> border.width
    3.1
    >>> border.height = 9.2
    >>> border.height
    9.2
    >>> border.width = "hello"
    Traceback (most recent call last):
    ...
    TypeError: width must be a number
    >>> border.height = "hello"
    Traceback (most recent call last):
    ...
    TypeError: height must be a number
    >>> border.width = -2
    Traceback (most recent call last):
    ...
    ValueError: width must be greater than zero
    >>> border.height = -6
    Traceback (most recent call last):
    ...
    ValueError: height must be greater than zero
    >>> border.width = 0
    Traceback (most recent call last):
    ...
    ValueError: width must be greater than zero
    >>> border.height = 0
    Traceback (most recent call last):
    ...
    ValueError: height must be greater than zero


Read-Only Properties
====================

Each `Border` object also provies read-only properties as follows:

* The `left` property gives the x-coordinate of the border's left side.
* The `right` property gives the x-coordinate of the border's right side.
* The `top` property gives the y-coordinate of the border's top side.
* The `bottom` property gives the y-coordinate of the border's bottom side.
* The `sides` property gives a 4-tuple of (left, right, bottom, top).

All of the properties above can only be read, but cannot be assigned to a new value.

The `left`, `right`, `bottom`, `top`, and `sides` properties are derived from
the main properties of a `Border` object.

    >>> border = Border(Vector(3, 4), 5, 6)
    >>> border
    Border(corner=Vector(x=3, y=4), width=5, height=6)
    >>> border.left
    3
    >>> border.right
    8
    >>> border.bottom
    4
    >>> border.top
    10
    >>> border.sides
    (3, 8, 4, 10)

However, these properties are read-only and cannot be updated directly.

    >>> border.left = 8
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> border.right = 2
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> border.bottom = 10
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> border.top = 5
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
