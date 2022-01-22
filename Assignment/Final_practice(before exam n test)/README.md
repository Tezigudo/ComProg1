# Final Practice Exercise

This practice assignment is meant for ensuring that your computer and Python
IDE can clone and submit your work on GitHub Classroom during the final
examination.

In this assignment, you are to implement the `person` module in the file
`person.py`.  The module contains the `Person` class that creates an object to
store a person's identification number and name using the
attributes/properties `id` and `name`, respectively.

    >>> from person import Person
    >>> p1 = Person('123-45', 'Tony Stark')
    >>> p2 = Person(id='777-77', name='Natasha Romanoff')
    >>> p1.name
    'Tony Stark'
    >>> p1.id
    '123-45'
    >>> p2.name
    'Natasha Romanoff'
    >>> p2.id
    '777-77'

String representation of a `Person` object is in the forms `Person(id=...,
name=...)` as shown.

    >>> p1
    Person(id='123-45', name='Tony Stark')
    >>> p2
    Person(id='777-77', name='Natasha Romanoff')

A `Person` object's `id` can only be set during the object construction.  An attempt to
assign a new value to `id` will cause an `AttributeError` exception to be raised, while
leaving the object unchanged.
(Hint: the `AttributeError` exception will be raised automatically if you
provide a getter for the `id` property without a setter.)

    >>> p1.id = '338-28'
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> p1
    Person(id='123-45', name='Tony Stark')

The `name` property can be reassigned to a new string.  An attempt to assign
it with a non-string value will cause a `TypeError` to be raised.

    >>> p1.name = 'Steve Rogers'
    >>> p1
    Person(id='123-45', name='Steve Rogers')
    >>> p1.name = 65535
    Traceback (most recent call last):
    ...
    TypeError: name must be a string

Data types of `id` and `name` are also checked during an object
initialization.

    >>> p3 = Person(98765, 'xxx')
    Traceback (most recent call last):
    ...
    TypeError: id must be a string

    >>> s4 = Person('333-33', 58)
    Traceback (most recent call last):
    ...
    TypeError: name must be a string


## Testing

To test the `person` module, run the `doctest` module against this `README.md` file.

    python -m doctest README.md

Alternatively, you can simply run the `person.py` file directly, which has a
`doctest` script included at the end of the code.

    python person.py
