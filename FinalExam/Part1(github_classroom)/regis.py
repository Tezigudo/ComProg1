class Regis:

    def __init__(self) -> None:
        self.students = {}
        self.courses = {}

    def add_student(self, new_students):
        self.students[new_students.id] = new_students

    def add_course(self, new_course):
        self.courses[new_course.id] = new_course

    def enroll(self, std_id, corse_id):
        self.students[std_id].course.append(self.courses[corse_id])
        self.courses[corse_id].std.append(self.students[std_id])

    def enrollments_by_student_id(self, std_id):
        return self.students[std_id].course

    def enrollments_by_course_id(self, corse_id):
        return self.courses[corse_id].std


if __name__ == '__main__':
    import doctest

    doctest.testfile('docs/regis.md')
