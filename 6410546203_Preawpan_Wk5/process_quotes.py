def read_file(filenames):
    """ Read file with filename
    Read one line as one string and return a list of string.

    :param filenames: str
    :return: a list of string
    """
    return open(filenames).read().splitlines()


def print_length(line):
    """ Display length of string (lines).
        Each line shows one string length and the string,
        separated by colon (:)
        and ended with comma (,).

    :param line: a list of string

    >>> print_length(['an', 'be', 'co'])
    2 : an,
    2 : be,
    2 : co,
    >>> print_length(['an', 'ant', 'a'])
    2 : an,
    3 : ant,
    1 : a,
    >>> print_length(['be', 'b', ''])
    2 : be,
    1 : b,
    0 : ,

    """
    for word in line:
        print(f'{len(word)} : {word},')


def search_by_index(text, index):
    """ Look for a character of string text at the given index

    :param text: str
    :param index: int
    :return: str

    >>> search_by_index('hello', 1)
    'e'
    >>> search_by_index('hello', 4)
    'o'
    >>> search_by_index('hi how are you', 2)
    ' '
    """
    return text[index]


def count(text, char):
    """ Count a number of character char inside string text

    :param text: str
    :param char: str
    :return: int

    >>> count('hello', 'l')
    2
    >>> count('hello', 's')
    0
    >>> count('banana', 'a')
    3
    """
    return sum(1 for letter in text if letter == char)


def find_char(text, char):
    """Find indexes of all character char found inside string text

    :param text: str
    :param char: str
    :return: a list of int

    >>> find_char('hello', 'l')
    [2, 3]
    >>> find_char('hello', 's')
    []
    >>> find_char('banana', 'a')
    [1, 3, 5]
    """
    return [i for i in range(len(text)) if text[i] == char]


def find_word(text, word):
    """ Look for string word inside string text
        If word is found, return True and a list of first index of each word
        If word is not found, return False and empty list

    :param text: str
    :param word: str
    :return: a list of int

    >>> find_word('banana', 'na')
    (True, [2, 4])
    >>> find_word('car care', 'car')
    (True, [0, 4])
    >>> find_word('banana', 'boat')
    (False, [])
    """

    def check(i):
        """

        :param i: index for loop(int)
        :return: None
        """
        if word.lower() == text[i:i+len(word)].lower():
            return True
        return False

    found = [i for i in range(len(text)-len(word)+1) if check(i)]

    return bool(found), found


def operate(liness, choices):
    """ Receive a list of string and user's choice
        Perform action corresponding to the choice

        :param liness: a list of string
        :param choices: int
    """

    if choices == 1:
        print_length(liness)
    elif choices == 2:
        index = int(input('Enter index: '))
        for line in liness:
            print(f'{search_by_index(line, index)} : {line}')
    elif choices == 3:
        char = input('Enter character: ')
        for line in liness:
            print(f'{count(lines, char)} : {line}')
    elif choices == 4:
        char = input('Enter character: ')
        for line in liness:
            print(f'{find_char(line, char)} : {line}')
    elif choices == 5:
        word = input('Enter a word: ')
        for line in liness:
            ind = find_word(line, word)
            print(f'{ind[1] if ind[0] else ""} : {line}')


filename = "quotes.txt"
lines = read_file(filename)
print('1. Print length')
print('2. Show character by index')
print('3. Count character')
print('4. Find character')
print('5. Find word')
choice = int(input('Enter choice: '))
operate(lines, choice)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
