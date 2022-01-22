'''This is a program as if a list of n players
take turn to move on board game. At each turn, the players will toss a
dice in a round robin style. The number obtained from dice will determine
how far each player can move alongthe board. After playing for m turns,
report which player walks the farthest distance as the winner.'''

from random import randrange


def initialize_list(Player_count: int) -> list:
    '''Ths function create and return list of Player_count zeros
    which show the each distance of player.'''

    return [0]*Player_count


def print_distance_list(distance_list: list[int]) -> None:
    '''print distance of all player'''

    for i in range(len(distance_list)):
        print(f'Player {i+1} : Distance = {distance_list[i]}')


def toss_dice() -> int:
    ''' Randomize integer between 1 and 6 (including 1 and 6).
    Return the random integer as if it is outcome of dice tossing.'''

    return randrange(1, 7)


def play_one_round(distance_list: list[int]) -> None:
    '''Allow player toses dice and update distance in each round'''

    for i in range(len(distance_list)):
        val = toss_dice()
        distance_list[i] += val
    print_distance_list(distance_list)


def play_all_rounds(Round_count: int, distance_list: list[int]) -> None:
    '''Repetitively play for Round_count rounds.'''

    print('Initializing...')
    print_distance_list(distance_list)
    print('Playing...')
    for rounds in range(1, Round_count+1):
        print(f'Round {rounds}:')
        play_one_round(distance_list)
    print('Game over...')


def find_winner(distance_list: list[int]) -> tuple:
    '''Return winning player and maximum distance of winning number'''

    max_dist = max(distance_list)
    winner = distance_list.index(max_dist)+1
    return winner, max_dist


def main() -> None:
    '''This function run a extire Program'''

    Player_count = int(input('Enter number of players: '))
    Round_count = int(input('Enter number of rounds: '))
    distance_list = initialize_list(Player_count)
    play_all_rounds(Round_count, distance_list)
    winner, max_dist = find_winner(distance_list)
    print(f'Player {winner} wins with maximum distance = {max_dist}')


if __name__ == '__main__':
    main()
