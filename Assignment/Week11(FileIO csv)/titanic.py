import csv

# open Titanic.csv file with csv.DictReader and read its content into a list of dictionary, titanic_data
titanic_data = []
with open('Titanic.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        titanic_data.append(r)


def number_single_embarked_survived(place_embarked: str, age_threshold: int,
                                    titanic_data: list) -> int:
    """Returns the number of survived single women over age_threshold embarked at place_embarked
    (Single women are denoted by "Miss")

    >>> number_single_embarked_survived("Southampton", 40, titanic_data)
    4
    >>> number_single_embarked_survived("Cherbourg", 50, titanic_data)
    2
    >>> number_single_embarked_survived("Queenstown", 20, titanic_data)
    3
    """

    return len(
        tuple(
            filter(
                # check if embarked is place_embarked
                lambda x: x['embarked'] == place_embarked
                          # check if prople have age or not if not age will be 0
                          # and compare with age threshold
                          and float(x['age'] or 0) > age_threshold
                          # check if people survived
                          and x['survived'] == 'yes'
                          # check if people is single girl
                          and 'Miss' in x['first'],
                titanic_data
            )
        )
    )


def exact_class(passenger_class: str, titanic_data: list) -> tuple:
    """
    exact where ever class 1, 2, or 3 people to tuple
    """
    return tuple(filter(lambda x: x['class'] == passenger_class, titanic_data))


def class_survival_rate(passenger_class: str, titanic_data: list) -> float:
    """Returns the survival rate of a given passenger_class

    >>> survival_rate = class_survival_rate("1", titanic_data)
    >>> f"{survival_rate:.2f}"
    '0.63'
    >>> survival_rate = class_survival_rate("2", titanic_data)
    >>> f"{survival_rate:.2f}"
    '0.47'
    >>> survival_rate = class_survival_rate("3", titanic_data)
    >>> f"{survival_rate:.2f}"
    '0.24'
    """

    all_class_peep = exact_class(passenger_class, titanic_data)

    # exact the survivor people into tuple
    survived = tuple(filter(lambda x: x['survived'] == 'yes', all_class_peep))

    return len(survived) / len(all_class_peep)  # return the rate of survivor


def average_class_fare(passenger_class: str, titanic_data: list) -> float:
    """Returns the average fare for a given class, 1, 2 or 3

    >>> average = average_class_fare("1", titanic_data)
    >>> f"{average:.2f}"
    '84.15'
    >>> average = average_class_fare("2", titanic_data)
    >>> f"{average:.2f}"
    '20.66'
    >>> average = average_class_fare("3", titanic_data)
    >>> f"{average:.2f}"
    '13.68'
    """

    all_class_peep = exact_class(passenger_class, titanic_data)

    # exact all fare from the people from specific class
    class_fare = [float(k['fare']) for k in all_class_peep]

    return sum(class_fare) / len(class_fare)


def gender_survival_number(passenger_gender: str, titanic_data: list) -> int:
    """Returns the number of survivors for a given gender, M (male) or F (female)

    >>> gender_survival_number('M', titanic_data)
    109
    >>> gender_survival_number('F', titanic_data)
    233
    """

    return len(tuple(filter(lambda x: x['gender'] == passenger_gender
                                      and x['survived'] == 'yes', titanic_data)))


def common_last_name(titanic_data: list) -> str:
    """Returns most common last name

    >>> common_last_name(titanic_data)
    'Andersson'
    """
    last = tuple(x['last'] for x in titanic_data)

    return max(last, key=lambda x: last.count(x))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
