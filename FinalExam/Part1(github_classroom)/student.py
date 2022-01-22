class Student:
    def __init__(self, id, name) -> None:
        self.name = name
        if not isinstance(id, str):
            raise TypeError('id must be a string')
        self.__id = id
        self.course = []

    def __repr__(self) -> str:
        return f"Student(id='{self.id}', name='{self.name}')"

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, other):
        if not isinstance(other, str):
            raise TypeError('name must be a string')
        self.__name = other


if __name__ == '__main__':
    import doctest

    doctest.testfile('docs/student.md')
