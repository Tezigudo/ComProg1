def display_reserved_seats(num_seat, seat_chart):
    """ Print seat chart showing reserved seats
        Comments are added below to explain how printing is done.

    :param num_seat: dictionary of str-int pairs
    :param seat_chart: dictionary of str-str pairs
    """
    max_num_seats = max(num_seat.values())
    # print header row
    print('   |', end='')
    for i in range(max_num_seats):
        print(f'{i + 1:3}|', end='')
    print()
    # print line between header row and reserved seats
    print('---|', end='')
    for i in range(max_num_seats):
        print('---|', end='')
    print()
    # print reserved seats
    for row in num_seat:
        # print row label
        print(f'{row:3}|', end='')
        for i in range(0, num_seat[row]):
            # show availability of each seat
            seat = row + str(i + 1)
            if seat_chart[seat] == '':
                print('   |', end='')
            else:
                print(' X |', end='')
        print()


def create_theater(row, num_seat):
    """ Construct seat chart (seat_chart) and guest reservation list (guests)
        This function is called once when the program starts.
        rows contains row labels (see Main part for declaration)
        num_seats is dictionary containing number of seats per row (see Main part for declaration)
        Return two dictionaries
        1) seat_chart: key is seat (str), and value is guest name (str).
                    Inititally, when seat is not reserved, value is empty string
        2) guests: key is guest name, value is list of reserved seat (str)
                    Inititally, guests will be empty.
        3) row_chart: key is seat (str), and value is row label (str).
                    Dictionary row_chart helps idenfity the row of each seat.

    :param row: list of str
    :param num_seat: dictionary of str-int pairs
    :return: Three dictionaries (see explanation above)

    >>> create_theater(['A', 'B'], {'A': 2, 'B': 3})
    ({'A1': '', 'A2': '', 'B1': '', 'B2': '', 'B3': ''}, {}, {'A1': 'A', 'A2': 'A', 'B1': 'B', 'B2': 'B', 'B3': 'B'})
    >>> create_theater(['X', 'Y'], {'X': 2, 'Y': 1})
    ({'X1': '', 'X2': '', 'Y1': ''}, {}, {'X1': 'X', 'X2': 'X', 'Y1': 'Y'})
    >>> create_theater(['VIP'], {'VIP': 4})
    ({'VIP1': '', 'VIP2': '', 'VIP3': '', 'VIP4': ''}, {}, {'VIP1': 'VIP', 'VIP2': 'VIP', 'VIP3': 'VIP', 'VIP4': 'VIP'})
    """
    seat_chart = {}
    guests = {}
    row_chart = {}
    for x in row:
        for i in range(num_seat[x]):
            seat = x + str(i + 1)
            seat_chart[seat] = ''
            row_chart[seat] = x
    return seat_chart, guests, row_chart


def reserve_seats(num_seat, seat_chart, guests):
    """ Reserve seats
        First, read guest name.  Create empty list of reserved seat for this guest.
        Then, continue reserving seats until user enters 'Q'
        If the entered seat is valid and not reserved,
           then put guest name in the seat chart
                add seat to list of reserved seat
        At the end, if guest reserves at least one seat,
            add list of reserved seat to guests dictionary
        Example: If John reserves 2 seats: 'A3' and 'A4',
                    then at the end, seat_chart['A3'] = 'John'
                                     seat_chart['A4'] = 'John'
                                     guests['John'] = ['A3', 'A4']


    ** Notice that in Python if we change values inside list or dictionary, we do not need to return **

    :param num_seat: dictionary of str-int pairs
    :param seat_chart: dictionary of str-str pairs
    :param guests: dictionary of str-list pairs
    """
    name = input('Enter name: ')
    guests[name] = [] if not guests.get(name) else guests[name]
    display_reserved_seats(num_seat, seat_chart)
    while True:
        tmp = input('Enter seat or (Q)uit: ')
        if tmp == 'Q':
            if guests[name]:
                print(f'{name} reserves {guests[name]}')
            else:
                del guests[name]
                print(f'{name} does not reserve seats.')
            break
        elif seat_chart.get(tmp, -1) == -1:
            print('This seat is invalid.')
        else:
            if not seat_chart[tmp]:
                guests[name].append(tmp)
                seat_chart[tmp] = name
                display_reserved_seats(num_seat, seat_chart)
            else:
                print('This seat is already reserved.')


def display_seat_chart(seat_chart):
    """ From seat chart, display seats that are reserved.
        At the end, show total seats and number of reserved seats

    :param seat_chart: dictionary of str-str pairs
    """
    reserved_count = sum(1 for x in seat_chart.values() if x)
    seat_count = len(seat_chart)
    for seat, name in seat_chart.items():
        if name:
            print(f'Seat {seat} is reserved by {name}')
    print(f'Total seats = {seat_count}')
    print(f'Number of reserved seats = {reserved_count}')


def display_guests(guests):
    """ From guests dictionary, show each guest reserves which seat.

    :param guests: dictionary of str-list pairs
    """
    for name, seat in guests.items():
        print(f'{name} reserves {seat}')


def compute_one_guest_payment(row_price, row_chart, guests, name):
    """ Compute payment for one guest with the given name.
        Note that name must exist inside guests dictionary before this function is called.

        row_prices is dictionary containing price for seats in each row. (see Main part for declaration)
        Note that seats in the same row cost the same price.

    :param row_price: dictionary of str-float pairs
    :param row_chart: dictionary of str-str pairs
    :param guests: dictionary of str-list pairs
    :param name: str
    :return float

    >>> compute_one_guest_payment({'A': 100, 'B': 50}, \
                                  {'A1': 'A', 'A2': 'A', 'B1': 'B'}, \
                                  {'John': ['A1', 'A2'], 'Jane': ['B1']}, \
                                  'John')
    200
    >>> compute_one_guest_payment({'A': 100, 'B': 50}, \
                                  {'A1': 'A', 'A2': 'A', 'B1': 'B'}, \
                                  {'John': ['A1', 'A2'], 'Jane': ['B1']}, \
                                  'Jane')
    50
    >>> compute_one_guest_payment({'X': 50.5, 'Y': 20.25, 'Z': 5.00}, \
                                  {'X1': 'X', 'Y1': 'Y', 'Y2': 'Y', 'Y3': 'Y', 'Y4': 'Y', 'Z1': 'Z'}, \
                                  {'Jack': ['Y1', 'Y2', 'Y3', 'Y4']}, \
                                  'Jack')
    81.0
    """
    return sum(row_price[row_chart[k]] for k in guests[name])


def report_all_payments(row_price, row_chart, guests):
    """ Report payment for all guests inside guests dictionary

    :param row_price: dictionary of str-float pairs
    :param row_chart: dictionary of str-str pairs
    :param guests: dictionary of str-list pairs
    """
    print('All payments:')
    for name in guests:
        price = compute_one_guest_payment(row_price, row_chart, guests, name)
        print(f'{name}: {price:.2f} Baht')


def cancel_one_seat_reservation(num_seat, seat_chart, guests):
    """ Cancel one seat reservation.
         First, read guest name.
         If the entered name is valid, continue to read until the entered name exists inside guests.
         If guest with the specific name has one reserved seat,
            remove this guest from guests dictionary and update seat_chart
         If guest with the specific name has more than one reserved seats,
            ask which seat he wants to cancel.
            The program will remove the seat only the entered seat exists in his reservation.
            If the entered seat does not exist, no seat is removed.

         Example: If John reserved 2 seats: 'A3' and 'A4', and he wants to cancel 'A4'
                     then at the end, seat_chart['A3'] = 'John'
                                      seat_chart['A4'] = ''
                                      guests['John'] = ['A3']

    ** Notice that in Python if we change values inside list or dictionary, we do not need to return **

    :param num_seat: dictionary of str-int pairs
    :param seat_chart: dictionary of str-str pairs
    :param guests: dictionary of str-list pairs
    """
    while True:
        name = input("Enter guest's name: ")
        if name in guests:
            seat = guests[name][0] if len(
                guests[name]) == 1 else input('Enter canceling seat: ')
            if seat in guests[name]:
                guests[name].remove(seat)
                seat_chart[seat] = ''
                display_reserved_seats(num_seat, seat_chart)
                if len(guests[name]) == 0:
                    del guests[name]
                if guests.get(name):
                    print(f'{name} reserves {guests[name]}')
                print('Canceling is done.')
            else:
                print(f'{name} did not reserve {seat}')
            break
        print(f'{name} does not exist.')


# Main part

"""
Below, two sets of theater information are given.  
You can use one set at a time to test your program. 
Your program should work with both sets.

Although only 2 sets of theater information are given,
        we can use other values for rows, num_seats, and row_prices when we grade your assignment.
Feel free to test your program with other values for rows, num_seats, and row_prices
You may want to edit function display_reserved_seats also if other values are used.
"""
# # Set 1
# rows = ['A', 'B', 'C', 'D', 'E']
# num_seats = {'A': 8, 'B': 8, 'C': 10, 'D': 10, 'E': 10}
# row_prices = {'A': 250, 'B': 200, 'C': 150, 'D': 150, 'E': 120}


# Set 2:
rows = ['VIP', 'X', 'Y']
num_seats = {'VIP': 4, 'X': 8, 'Y': 12}
row_prices = {'VIP': 1000, 'X': 500, 'Y': 200}


def main():
    seat_chart, guests, row_chart = create_theater(rows, num_seats)
    while True:

        print('1. Reserve seats')
        print('2. Display seat information')
        print('3. Display guest information')
        print('4. Get payment for one guest')
        print('5. Display payments for all guests')
        print('6. Cancel one seat reservation')
        print('7. Exit program')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            reserve_seats(num_seats, seat_chart, guests)
        elif choice == 7:
            break
        else:
            if not guests:
                print('No guest reservation.')
            else:
                if choice == 2:
                    display_seat_chart(seat_chart)
                elif choice == 3:
                    display_guests(guests)
                elif choice == 4:
                    display_guests(guests)
                    while True:
                        name = input("Enter guest's name: ")
                        if name not in guests:
                            print(f'{name} does not exist.')
                        else:
                            print(f'Payment for {name} = '
                                  f'{compute_one_guest_payment(row_prices, row_chart, guests, name):.2f} Baht.')
                            break
                elif choice == 5:
                    report_all_payments(row_prices, row_chart, guests)
                elif choice == 6:
                    display_guests(guests)
                    cancel_one_seat_reservation(num_seats, seat_chart, guests)
        print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
