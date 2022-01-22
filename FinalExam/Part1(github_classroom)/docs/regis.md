## The `regis.py` Module

The `regis.py` module implements the `Regis` class for creating an object to keep track of students, courses, and
students' enrollments to courses in the system. This module depends on the `student.py` and `course.py` modules to work.

Each `Regis` object maintains an attribute `students`, which is a dict of
`Student` objects, and an attribute `courses`, which is a dict of `Course`
objects. Both dicts are initially empty.

    >>> from student import Student
    >>> from course import Course
    >>> from regis import Regis

    >>> reg = Regis()
    >>> reg.students
    {}
    >>> reg.courses
    {}

The `add_student` method takes a `Student` object as an argument and stores the object in the `students` dict with the
student's id as the key.

    >>> reg.add_student(Student('1234', 'Albert Einstein'))
    >>> reg.add_student(Student('5555', 'Marie Curie'))
    >>> reg.students['1234']
    Student(id='1234', name='Albert Einstein')
    >>> reg.students['5555']
    Student(id='5555', name='Marie Curie')

An attempt to access a non-existing student will result in a `KeyError`
exception.  (Hint: this exception is automatically raised by Python's dict, so you shouldn't have to do anything.)

    >>> reg.students['8888']
    Traceback (most recent call last):
    ...
    KeyError: '8888'

Similarly, the `add_course` method takes a `Course` object as an argument and stores, the object in the `courses` dict
with the course's id as the key.

    >>> reg.add_course(Course('ske114', 'Programming 1', 3))
    >>> reg.add_course(Course('mat111', 'Math 1', 3))
    >>> reg.courses['ske114']
    Course(id='ske114', name='Programming 1', credits=3)
    >>> reg.courses['mat111']
    Course(id='mat111', name='Math 1', credits=3)

For enrollments, the `enroll` method enrolls a student to a course by taking a student's id and a course's id as
arguments. How the enrollment information is stored in a `Regis` object is up to you.

    >>> reg.enroll('1234', 'ske114')
    >>> reg.enroll('1234', 'mat111')
    >>> reg.enroll('5555', 'ske114')

The `enrollments_by_student_id` method takes a student's id as an argument and returns a list of courses in which the
student are enrolled.

    >>> reg.enrollments_by_student_id('1234')
    [Course(id='ske114', name='Programming 1', credits=3), Course(id='mat111', name='Math 1', credits=3)]
    >>> reg.enrollments_by_student_id('5555')
    [Course(id='ske114', name='Programming 1', credits=3)]

Similarly, the `enrollments_by_course_id` method takes a course's id as an argument and returns a list of enrolled
students.

    >>> reg.enrollments_by_course_id('ske114')
    [Student(id='1234', name='Albert Einstein'), Student(id='5555', name='Marie Curie')]
    >>> reg.enrollments_by_course_id('mat111')
    [Student(id='1234', name='Albert Einstein')]

## Testing

To test the `regis.py` module, run the `doctest` module against this `regis.md` file.

    python -m doctest docs/regis.md

Alternatively, you can simply run the `regis.py` file directly, which has a
`doctest` script included at the end of the code.

    python regis.py
