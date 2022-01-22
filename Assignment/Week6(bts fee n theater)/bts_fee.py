def read_file(filename):
    """ Read file with filename
        Read one line of station code and station name
        At the end, each row in table contains 2 strings (code and name).
        Number of rows in table = number of stations

    :param filename: str
    :return: nested list of str
    """
    lines = open(filename).read().splitlines()
    table = [x.split(",") for x in lines if x != ""]
    return table


def create_station_names(table):
    """ Receive nested list of station code and station name
        Convert to dictionary where station code is key, station name is value
        Return this dictionary

    :param table: nested list of str
    :return: dictionary
    >>> create_station_names([['E3', 'Nana'], ['E4','Asok'], ['E5', 'Phrom Phong']])
    {'E3': 'Nana', 'E4': 'Asok', 'E5': 'Phrom Phong'}
    >>> create_station_names([['N20','Saphan Mai'], ['N19','Sai Yud']])
    {'N20': 'Saphan Mai', 'N19': 'Sai Yud'}
    >>> create_station_names([[]])
    {}
    """
    return {} if not table[0] else dict(table)


def extract_station_code(station_code):
    """ Receive station code
        Return station line and station index
        For station code CEN.

    :param station_code: str
    :return: int and str
    >>> extract_station_code('N13')
    ('N', 13)
    >>> extract_station_code('E9')
    ('E', 9)
    >>> extract_station_code('CEN')
    ('N', 0)
    """
    d = ''.join(k for k in station_code if k.isdigit())
    return ''.join(k for k in station_code if k.isalpha())[-1], \
           int([0, d][bool(d)])


def count_num_stations(base_stations, curr_station):
    """ Receive a list of base stations and current station code
        Find number of stations between current station and each base station.
        Note that base_stations in this problem is fixed, unlike doctest cases.

        Return dictionary where key is station code,
                          value is number of stations between key station and current station code
        Example: number of stations between N2-N2 = 0
                 number of stations between N1-N2 = 1

    :param base_stations: a list of str
    :param curr_station: str
    :return: dictionary
    >>> count_num_stations(['N1', 'N2', 'N3', 'N4'], 'N2')
    {'N1': 1, 'N2': 0, 'N3': 1, 'N4': 2}
    >>> count_num_stations(['E9', 'E8', 'E7', 'E6', 'E5'], 'E7')
    {'E9': 2, 'E8': 1, 'E7': 0, 'E6': 1, 'E5': 2}
    >>> count_num_stations(['N2', 'N1', 'CEN', 'E1', 'E2', 'E3'], 'E1')
    {'N2': 3, 'N1': 2, 'CEN': 1, 'E1': 0, 'E2': 1, 'E3': 2}
    """
    return dict([[base_stations[i], abs(base_stations.index(curr_station) - i)]
                for i in range(len(base_stations))])


def get_num_station_grid(base_stations):
    """ Receive a list of base stations
        Create a nested dictionary grid such that
            grid[X][Y] = number of stations between stations X and Y
            X and Y are stations inside base_stations.
        Example: grid['N8']['N1'] = 7
                 grid['N8']['CEN'] = 8
                 grid['N8']['E2'] = 10

    :param base_stations: a list of str
    :return: nested dictionary
    >>> get_num_station_grid(['N2', 'N3'])
    {'N2': {'N2': 0, 'N3': 1}, 'N3': {'N2': 1, 'N3': 0}}
    >>> get_num_station_grid(['E9', 'E8', 'E7'])
    {'E9': {'E9': 0, 'E8': 1, 'E7': 2}, 'E8': {'E9': 1, 'E8': 0, 'E7': 1}, 'E7': {'E9': 2, 'E8': 1, 'E7': 0}}
    >>> get_num_station_grid(['N2', 'N1', 'CEN', 'E1'])
    {'N2': {'N2': 0, 'N1': 1, 'CEN': 2, 'E1': 3}, 'N1': {'N2': 1, 'N1': 0, 'CEN': 1, 'E1': 2}, 'CEN': {'N2': 2, 'N1': 1, 'CEN': 0, 'E1': 1}, 'E1': {'N2': 3, 'N1': 2, 'CEN': 1, 'E1': 0}}
    """
    return {k: count_num_stations(base_stations, k) for k in base_stations}


def read_station(base_stations, extension_stations, text):
    """ Read station code from user
        The station code must be one of base stations or extension staitons.
        If the station is not one of base stations or extension staitons, continue reading.
        Note that text is a string that can be either 'origin' or 'destination'
        Return the valid station code.

    :param base_stations: a list of str
    :param extension_stations: a list of str
    :param text: str
    :return: str
    """
    while True:
        now = input(f'Enter {text} station (N24-E9): ')
        if now in base_stations + extension_stations:
            return now
        print(f'Station {now} does not exist. Enter a station between N24-E9.')


def get_base_fee(num_station_grid, origin, dest):
    """ Compute fee inside the base station zone, given origin and destination station code
        Return the fee

    :param num_station_grid: nested dictionary
    :param origin: str
    :param dest: str
    :return: int
    >>> get_base_fee({'E9': {'E9': 0, 'E8': 1, 'E7': 2}, 'E8': {'E9': 1, 'E8': 0, 'E7': 1}, 'E7': {'E9': 2, 'E8': 1, 'E7': 0}}, 'E9', 'E8')
    16
    >>> get_base_fee({'E9': {'E9': 0, 'E8': 1, 'E7': 2}, 'E8': {'E9': 1, 'E8': 0, 'E7': 1}, 'E7': {'E9': 2, 'E8': 1, 'E7': 0}}, 'E9', 'E7')
    23
    >>> get_base_fee({'N2': {'N2': 0, 'N1': 1, 'CEN': 2, 'E1': 3}, 'N1': {'N2': 1, 'N1': 0, 'CEN': 1, 'E1': 2}, 'CEN': {'N2': 2, 'N1': 1, 'CEN': 0, 'E1': 1}, 'E1': {'N2': 3, 'N1': 2, 'CEN': 1, 'E1': 0}}, 'N2', 'E1')
    26
    """

    def fee(station_dist):
        if station_dist < 2:
            return 16
        elif station_dist > 8:
            return 44
        elif station_dist == 2:
            return 23
        elif not station_dist % 2:
            return fee(station_dist - 1) + 4
        else:
            return fee(station_dist - 1) + 3

    return fee(num_station_grid[origin][dest])


def get_extension_fee(origin, dest):
    """ Compute fee inside the extension station zone, given origin and destination station code
        Return the fee

    :param origin: str
    :param dest: str
    :return: int
    >>> get_extension_fee('N9', 'N13')
    27
    >>> get_extension_fee('N20', 'N12')
    39
    >>> get_extension_fee('N10', 'N10')
    15
    """
    num_origin = extract_station_code(origin)[1]
    num_dest = extract_station_code(dest)[1]

    return 15 + 3 * abs(num_dest - num_origin)


def compute_fee(num_station_grid, base_stations,
                extension_stations, origin, dest):
    """ Compute and return BTS fee from origin station code to destination station code

    :param num_station_grid: nested dictionary
    :param base_stations: a list of str
    :param extension_stations: a list of str
    :param origin: str
    :param dest: str
    :return: int
    """
    if origin in extension_stations and dest in extension_stations:
        return get_extension_fee(origin, dest)

    if origin in base_stations and dest in base_stations:
        return get_base_fee(num_station_grid, origin, dest)

    if origin in base_stations:
        return get_base_fee(num_station_grid, origin, 'N8') \
            + get_extension_fee('N9', dest) - 15

    return get_base_fee(num_station_grid, 'N8', dest) + get_extension_fee(origin, 'N9') - 15


def initialize():
    """
    :return:
    """
    base_stations = ['N' + str(i) for i in range(8, 0, -1)] + \
                    ['CEN'] + ['E' + str(i) for i in range(1, 10)]
    extension_stations = ['N' + str(i) for i in range(24, 8, -1)]
    filename = 'bts_station_list.txt'
    table = read_file(filename)
    station_names = create_station_names(table)
    num_station_grid = get_num_station_grid(base_stations)

    return num_station_grid, base_stations, extension_stations, station_names


def main():
    """This function run an entire Program"""
    num_station_grid, base_stations, extension_stations, station_names = initialize()
    count = 1
    total = 0
    while True:
        print(f'Ticket{count}:')
        origin = read_station(base_stations, extension_stations, 'origin')
        dest = read_station(base_stations, extension_stations, 'destination')
        price = compute_fee(num_station_grid, base_stations,
                            extension_stations, origin, dest)

        if origin in extension_stations and dest in extension_stations:
            print(
                f'Extension Station Zone: Fee = {get_extension_fee(origin, dest)} Baht')
        elif origin in base_stations and dest in base_stations:
            print(
                f'Base Station Zone: Fee = {get_base_fee(num_station_grid, origin, dest)} Baht')
        elif origin in base_stations:
            print(
                f'Base Station Zone: Fee = {get_base_fee(num_station_grid, origin, "N8")} Baht')
            print(
                f'Extension Station Zone: Fee = {get_extension_fee("N9", dest)} Baht')
        else:
            print(
                f'Extension Station Zone: Fee = {get_extension_fee(origin, "N9")} Baht')
            print(
                f'Base Station Zone: Fee = {get_base_fee(num_station_grid, "N8", dest)} Baht')

        print(f'Origin = {origin} = {station_names[origin]},'
              f'Destination = {dest} = {station_names[dest]}: Fee = {price}')
        total += price
        print()
        choice = input('Do you want to continue (Y/N)? ')
        print()
        if choice == 'Y':
            count += 1
            continue
        elif choice == 'N':
            print(f'{count} tickets are sold.')
            print(f'{total} Baht is collected.')
            break
        else:
            raise ValueError('Invalid input')


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
