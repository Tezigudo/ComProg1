## The `student.py` Module

The `student.py` module implements the `Student` class for creating an object to store a student's identification number
and name using the attributes/properties `id` and `name`, respectively.

    >>> from student import Student
    >>> s1 = Student('1234', 'Albert Einstein')
    >>> s2 = Student('5555', 'Marie Curie')
    >>> s1.name
    'Albert Einstein'
    >>> s1.id
    '1234'

String representation of a `Student` object is in the forms `Student(id=..., name=...)` as shown.

    >>> s1
    Student(id='1234', name='Albert Einstein')
    >>> s2
    Student(id='5555', name='Marie Curie')

A `Student` object's `id` can only be set during the object construction. An attempt to assign a new value to `id` will
cause an `AttributeError` exception to be raised, while leaving the object unchanged.  (Hint: the `AttributeError`
exception will be raised automatically if you provide a getter for the `id`
property without a setter.)

    >>> s1.id = '3388'
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> s1
    Student(id='1234', name='Albert Einstein')

The `name` property can be reassigned to a new string. An attempt to assign it with a non-string value will cause
a `TypeError` to be raised.

    >>> s1.name = 'Nikola Tesla'
    >>> s1
    Student(id='1234', name='Nikola Tesla')

    >>> s1.name = 99
    Traceback (most recent call last):
    ...
    TypeError: name must be a string

## Testing

To test the `student.py` module, run the `doctest` module against this `student.md` file.

    python -m doctest docs/student.md

Alternatively, you can simply run the `student.py` file directly, which has a
`doctest` script included at the end of the code.

    python student.py
