class Course:
    def __init__(self, id, name, credits) -> None:
        self.__id = id
        self.name = name
        self.credits = credits
        self.std = []

    def __repr__(self) -> str:
        return f"Course(id='{self.id}', name='{self.name}', credits={self.credits})"

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

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, other):
        if not isinstance(other, int):
            raise TypeError('credits must be an integer')
        if other <= 0:
            raise ValueError('credits must be positive')
        self.__credits = other


if __name__ == '__main__':
    import doctest

    doctest.testfile('docs/course.md')
