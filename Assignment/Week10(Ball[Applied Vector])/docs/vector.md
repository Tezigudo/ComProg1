# Module `vector.py`

The module `vector.py` defines the `Vector` class.

    >>> from vector import Vector

Initialization
==============

Each `Vector` object contains two properties: `x` and `y`.

    >>> type(Vector.x)
    <class 'property'>
    >>> type(Vector.y)
    <class 'property'>

They can be optionally initialized via the constructor.

    >>> v1 = Vector(x=3, y=6)
    >>> v1.x, v1.y
    (3, 6)

If no initial value is provided, the default value of zero is assigned.

    >>> v2 = Vector()
    >>> v2.x, v2.y
    (0, 0)
    >>> v3 = Vector(x=5)
    >>> v3.x, v3.y
    (5, 0)
    >>> v4 = Vector(y=2)
    >>> v4.x, v4.y
    (0, 2)


Property Validation
===================

The properties `x` and `y` can only be assigned with numbers.  Other types will
cause a `TypeError` to be raised.

    >>> u = Vector(2, 5)
    >>> u.x, u.y
    (2, 5)
    >>> u.x = 3
    >>> u.x
    3
    >>> u.y = -5.8
    >>> u.y
    -5.8
    >>> u.x = "hello"
    Traceback (most recent call last):
    ...
    TypeError: The x attribute must be a number
    >>> u.y = "goodbye"
    Traceback (most recent call last):
    ...
    TypeError: The y attribute must be a number


String Representation
=====================

When represented as a string, a `Vector` object displays the values of its `x`
and `y` properties as shown:

    >>> v1 = Vector(3, 4)
    >>> v1
    Vector(x=3, y=4)
    >>> print(v1)
    Vector(x=3, y=4)
    >>> v2 = Vector()
    >>> v2
    Vector(x=0, y=0)
    >>> print(v2)
    Vector(x=0, y=0)


Vector's Methods
================

The `length` method returns the length of the vector.

    >>> u = Vector(3, 4)
    >>> v = Vector(5, 12)
    >>> u.length()
    5.0
    >>> v.length()
    13.0

The `dot` method computes the dot product of the current vector and the
specified vector.

    >>> u = Vector(3, 4)
    >>> v = Vector(5, 2)
    >>> u.dot(v)
    23
    >>> v.dot(u)
    23
    >>> print(u, v)
    Vector(x=3, y=4) Vector(x=5, y=2)


Math Operations
===============

We can add or subtract two Vector objects using the `+` and `-` operators,
respectively.  Each operation must return a new `Vector` object and must not
affect the original `Vector` objects.

    >>> u = Vector(2, 5)
    >>> v = Vector(3, 8)
    >>> w1 = v + u
    >>> w1
    Vector(x=5, y=13)
    >>> w2 = v - u
    >>> w2
    Vector(x=1, y=3)
    >>> w3 = v - u + u - v
    >>> w3
    Vector(x=0, y=0)
    >>> u
    Vector(x=2, y=5)
    >>> v
    Vector(x=3, y=8)

We can scale a `Vector` object using the `*` operator with a scalar (i.e., a
regular number).  Each operation must return a new Vector object and must not
affect the original Vector objects.  The operator `*` must allow a scaling
operand to be applied both on the left side or the right side.

    >>> u = Vector(3, 6)
    >>> v = Vector(4, 10)
    >>> w1 = u*2
    >>> w1
    Vector(x=6, y=12)
    >>> w2 = 2*v
    >>> w2
    Vector(x=8, y=20)
    >>> w3 = (1/3)*u + (1/2)*v
    >>> w3
    Vector(x=3.0, y=7.0)
