def read_file(filenames):
    """ Read file with filename
        Read one line of student information and return a list of string.

    :param filenames: str
    :return: a list of string
    """
    lines = open(filenames).read().splitlines()
    tables = [x.split(",") for x in lines if x != ""]
    return tables


def extract_name_lists(tables):
    """ Receive nested list of string
        Return the first two columns of string as two separate lists,
        but exclude the first row

    :param tables: nested_list of str
    :return: two lists of str
    >>> extract_name_lists([['FirstName', 'Lastname', 'Grade'],['Ann', 'Smith', 'B+'],['Barry', 'Williams', 'C+']])
    (['Ann', 'Barry'], ['Smith', 'Williams'])
    >>> extract_name_lists([['FirstName', 'Lastname'],['Cathy', 'Johnson'],['David', 'Jones'],['Eric', 'Garcia']])
    (['Cathy', 'David', 'Eric'], ['Johnson', 'Jones', 'Garcia'])
    >>> extract_name_lists([['FirstName', 'Lastname', '101', '102'],['Irene', 'Wilson', 'B', 'B+']])
    (['Irene'], ['Wilson'])
    """
    return [first_name[0] for first_name in tables[1:]],\
           [last_name[1] for last_name in tables[1:]]


def extract_course_list(tables):
    """ Receive nested list of string
        Return the first row (course names), but not the first two members (first name and last name)

    :param tables: nested_list of str
    :return: a list of str
    >>> extract_course_list([['FirstName', 'Lastname', '01219114'],['Ann', 'Smith', 'B+'],['Barry', 'Williams', 'C+']])
    ['01219114']
    >>> extract_course_list([['FirstName', 'Lastname', '101', '102'],['Irene', 'Wilson', 'B', 'B+']])
    ['101', '102']
    >>> extract_course_list([['FirstName', 'Lastname'],['Cathy', 'Johnson'],['David', 'Jones'],['Eric', 'Garcia']])
    []
    """

    return tables[0][2:]


def convert_one_grade_point(grade):
    """ Receive one letter grade and return a point grade.

    :param grade: str
    :return: float
    >>> convert_one_grade_point('A')
    4.0
    >>> convert_one_grade_point('D+')
    1.5
    >>> convert_one_grade_point('F')
    0.0
    """

    grade_index = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F'].index(grade)
    if grade_index == 7:
        return 0.0

    return 4.0-(0.5*grade_index)


def convert_all_grade_points(grade_str_table):
    """ Receive nested list of letter grades and convert to point grades
        Return

    :param grade_str_table: nested_list of str
    :return: nested_list of float
    >>> convert_all_grade_points([['A','B'], ['B+','C']])
    [[4.0, 3.0], [3.5, 2.0]]
    >>> convert_all_grade_points([['D+','D','C+']])
    [[1.5, 1.0, 2.5]]
    >>> convert_all_grade_points([['F'], ['A'], ['B+']])
    [[0.0], [4.0], [3.5]]
    """
    return [[convert_one_grade_point(grade) for grade in person_grade] for person_grade in grade_str_table]


def get_grade_point_table(tables):
    """ Receive nested list of string containing letter grades of all students, all courses
        Return nested list of float containing point grades of all students, all courses

    :param tables: nested list of str
    :return: nested list of float
    >>> get_grade_point_table([['FirstName', 'Lastname', '01219114'],['Ann', 'Smith', 'B+'],['Barry', 'Williams', 'C+']])
    [[3.5], [2.5]]
    >>> get_grade_point_table([['FirstName', 'Lastname', '101', '102'],['Irene', 'Wilson', 'B', 'B+']])
    [[3.0, 3.5]]
    >>> get_grade_point_table([['FirstName', 'Lastname'],['Cathy', 'Johnson'],['David', 'Jones'],['Eric', 'Garcia']])
    [[], [], []]
    """
    return convert_all_grade_points([grade[2:] for grade in tables[1:]])


def compute_ave_student_grade(grade_point_tables):
    """ Receive nested list of float, containing point grades of all students, all courses
        Return the list of average grade for each student

    :param grade_point_tables: nested list of float
    :return: a list of float
    >>> compute_ave_student_grade([[0.0, 0.0, 0.0], [4.0, 3.5, 1.5]])
    [0.0, 3.0]
    >>> compute_ave_student_grade([[2.0, 1.0], [4.0, 1.5], [2.0, 1.0]])
    [1.5, 2.75, 1.5]
    >>> compute_ave_student_grade([[1.0], [0.0], [4.0], [2.5]])
    [1.0, 0.0, 4.0, 2.5]
    """
    return [sum(score) / len(score) for score in grade_point_tables]


def compute_ave_course_grade(grade_point_tables):
    """ Receive nested list of float, containing point grades of all students, all courses
        Return the list of average grade for each course

    :param grade_point_tables: nested list of float
    :return: compute_ave_course_grade
    >>> compute_ave_course_grade([[0.0, 0.0, 0.0], [4.0, 3.5, 1.5]])
    [2.0, 1.75, 0.75]
    >>> compute_ave_course_grade([[2.0, 1.0], [4.0, 1.5], [2.0, 1.0]])
    [2.6666666666666665, 1.1666666666666667]
    >>> compute_ave_course_grade([[1.0], [0.0], [4.0], [2.5]])
    [1.875]
    """
    return compute_ave_student_grade(list(zip(*grade_point_tables)))


def find_item_list(item_list, search_str):
    """ Receive a list of items (item_list) and string to be searched (search_str)
        Return a list containing indexes of string that matche the search_str

    :param item_list: a list of str
    :param search_str: str
    :return: a list of int
    >>> find_item_list(['Ann', 'Barry', 'Cathy'], 'Ann')
    [0]
    >>> find_item_list(['Ann', 'Barry', 'Ann', 'Cathy'], 'Ann')
    [0, 2]
    >>> find_item_list(['Ann', 'Barry', 'Cathy'], 'David')
    []
    >>> find_item_list(['01420111', '01219114', '01355112', '01417167'], '01219114')
    [1]
    """
    return [i for i in range(len(item_list)) if item_list[i] == search_str]


def get_column_list(nested_list, index):
    """ Receive nested list of numbers and a column index
        Return a list of numbers from the column with the given column index

    :param nested_list: nested list of floats
    :param index: int
    :return: a list of float
    >>> get_column_list([[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]], 2)
    [3, 8, 13]
    >>> get_column_list([[13, 15, 17], [28, 26, 24]], 1)
    [15, 26]
    >>> get_column_list([[6, 12, 18]], 0)
    [6]
    """
    return [row[index] for row in nested_list]


def find_below_index_list(item_list, threshold):
    """ Receive a list of numbers (item_list) and a threshold value
        Return a list of indexes corresponding to numbers that are less than the threshold
    :param item_list: a list of floats
    :param threshold: float
    :return: a list of int
    >>> find_below_index_list([4.0, 3.5, 2.0, 1.5], 2.0)
    [3]
    >>> find_below_index_list([28, 26, 24], 27.0)
    [1, 2]
    >>> find_below_index_list([6, 12, 18], 5.0)
    []
    """
    return [i for i in range(len(item_list)) if item_list[i] < threshold]


def print_partial_students(firstname_lists, lastname_lists, course_lists, grade_point_tables, index_list):
    """ Receive a list of first names, last names, course numbers, and grade point table.
        Also receive a list of row indexes.
        Show student information from the given rows
    :param firstname_lists: a list of strings
    :param lastname_lists: a list of strings
    :param course_lists: a list of strings
    :param grade_point_tables: nested list of floats
    :param index_list: a list of int
    """
    print('                     : ', end='')
    for j in range(len(course_lists)):
        print(f'{course_lists[j]:8}', end=' ')
    print()
    for i in range(len(index_list)):
        print(f'{firstname_lists[index_list[i]]:10} {lastname_lists[index_list[i]]:10}: ', end='')
        for j in range(len(course_lists)):
            print(f'{grade_point_tables[index_list[i]][j]:8}', end=' ')
        print()


def operate(firstname_lists, lastname_lists,
            course_lists, grade_point_tables, choices):
    """ Receive a list of first names, last names, course numbers, and grade point table.
        Also receive user's choice as int.
        Perform action corresponding to the choice

    :param firstname_lists: a list of strings
    :param lastname_lists: a list of strings
    :param course_lists: a list of strings
    :param grade_point_tables: nested list of floats
    :param choices: int
    """

    if choices == 1:
        average_grade = compute_ave_student_grade(grade_point_tables)
        for i in range(len(firstname_lists)):
            print(f'{firstname_list[i]} {lastname_list[i]} : {average_grade[i]:.2f}')
    elif choices == 2:
        for i in range(len(course_lists)):
            print(f'{course_lists[i]} : {compute_ave_course_grade(grade_point_tables)[i]:.2f}')
    elif choices == 3:
        name = input('Enter name to search: ')
        print_partial_students(firstname_lists, lastname_lists,
                               course_lists, grade_point_tables,
                               find_item_list(firstname_lists, name))
    elif choices == 4:
        course = input('Enter course to search: ')
        threshold = float(input('Enter threshold: '))
        course_index = course_lists.index(course)
        col_list = get_column_list(grade_point_tables, course_index)
        print_partial_students(firstname_lists, lastname_lists, course_lists,
                               grade_point_tables, find_below_index_list(col_list, threshold))


filename = "students_large.txt"
table = read_file(filename)

firstname_list, lastname_list = extract_name_lists(table)
course_list = extract_course_list(table)
grade_point_table = get_grade_point_table(table)

print('1. Compute average student grades')
print('2. Compute average course grades')
print('3. Find grades by first name')
print('4. Find students with below grade')
choice = int(input('Enter choice: '))
operate(firstname_list, lastname_list, course_list, grade_point_table, choice)

if __name__ == "__main__":
    import doctest
    doctest.testmod()



# def find_e(times):
#     for i in range(1, times+1):
#         print(f'{i} | {(1+(1/i))**i}')

# find_e(10**6)
# # def find_e_n(n):
# #     return (1+(1/n))**n

# print(find_e_n(10**12))


# import pandas as pd

# files = pd.read_csv("students_large.csv")
# x = pd.DataFrame(files)
# print(x['Lastname'])