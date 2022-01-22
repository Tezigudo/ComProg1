## The `course.py` Module

The `course.py` module implements the `Course` class for creating an object to store a course's identification number,
name, and credits, using the attributes/properties `id`, `name`, and `credits`, respectively.

    >>> from course import Course
    >>> c1 = Course('ske114', 'Programming 1', 3)
    >>> c2 = Course('mat111', 'Math 1', 3)
    >>> c3 = Course('ske115', 'Programming 1 Lab', 1)
    >>> c1.id
    'ske114'
    >>> c1.name
    'Programming 1'
    >>> c1.credits
    3

String representation of a `Course` object is in the forms `Course(id=..., name=..., credits=...)` as shown.

    >>> c1
    Course(id='ske114', name='Programming 1', credits=3)
    >>> c2
    Course(id='mat111', name='Math 1', credits=3)
    >>> c3
    Course(id='ske115', name='Programming 1 Lab', credits=1)

A `Course` object's `id` can only be set during the object construction. An attempt to assign a new value to `id` will
cause an `AttributeError` exception to be raised, while leaving the object unchanged.  (Hint: the `AttributeError`
exception will be raised automatically if you provide a getter for the `id`
property without a setter.)

    >>> c1.id = 'xxx'
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> c1
    Course(id='ske114', name='Programming 1', credits=3)

The `name` property can be reassigned to a new string. An attempt to assign it with a non-string value will cause
a `TypeError` to be raised.

    >>> c1.name = 'Computer Programming I'
    >>> c1.name
    'Computer Programming I'

    >>> c1.name = 88
    Traceback (most recent call last):
    ...
    TypeError: name must be a string

The `credits` property can be reassigned to a new positive integer. An attempt to assign it with a non-integer value
will result in a `TypeError` exception. If the given integer is zero or negative, a `ValueError` exception is raised.

    >>> c1.credits = 2
    >>> c1.credits
    2

    >>> c1.credits = '50'
    Traceback (most recent call last):
    ...
    TypeError: credits must be an integer

    >>> c1.credits = 0
    Traceback (most recent call last):
    ...
    ValueError: credits must be positive

## Testing

To test the `course.py` module, run the `doctest` module against this `course.md` file.

    python -m doctest docs/course.md

Alternatively, you can simply run the `course.py` file directly, which has a
`doctest` script included at the end of the code.

    python course.py
