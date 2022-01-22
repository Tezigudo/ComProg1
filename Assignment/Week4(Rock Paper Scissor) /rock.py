'''This is a program for two teams to play rock,
paper and scissors. At the end, the program reports which team
has the most number of wins.'''

from random import randrange
__author__ = 'Preawpan Thamapipol'
__version__ = '1.0'


def initialize_list(Player_count: int) -> list:
    '''Ths function create and return list of Player_count zeros
    which illustrate the each distance of player'''

    return [0]*Player_count


def print_two_team_stat(team_1: list[int], team_2: list[int]) -> None:
    '''This function Print win list of two teams.'''

    print(f'Team 1: {team_1}')
    print(f'Team 2: {team_2}')


def randomize_player(Player_count: int) -> int:
    '''This function Randomize an integer between 1 and Player_count'''

    return randrange(1, len(Player_count)+1)


def randomize_hand() -> str:
    '''Randomize integer between 1 and 3 (including 1 and 3).
    If random number is 1, return “Rock”
    If random number is 2, return “Paper”
    If random number is 3, return “Scissors”'''
    rand_num = randrange(1, 4)

    return ['Rock', 'Paper', 'Scissors'][rand_num-1]


def find_round_winner(hand1: str, hand2: str) -> int:
    ''' From hands of two players,
        find out who is the round winner.
        If team1 player wins, return 1.
        If team2 player wins, return 2.
        If the players tie, return 0.'''

    if hand1 == hand2:
        return 0
    elif (hand1 == 'Rock' and hand2 == 'Scissors') \
            or (hand1 == 'Paper' and hand2 == 'Rock') \
            or (hand1 == 'Scissors' and hand2 == 'Paper'):
        return 1
    else:
        return 2


def report_winner(winner: int) -> None:
    '''This function Display which team wins, or both teams tie.'''
    if not winner:
        print('Both teams tie.')
    elif winner == 1:
        print('Team 1 wins.')
    else:
        print('Team 2 wins.')


def play_one_round(team_1: list[int], team_2: list[int]) -> None:
    '''This function Randomly choose one player from each team to play.
    Then, find out and report the round winner. After that,
    update and report the statistics.'''

    player_from_team_1 = randomize_player(team_1)-1
    player_from_team_2 = randomize_player(team_2)-1
    player_1_choose = randomize_hand()
    player_2_choose = randomize_hand()

    print(f'Team1: Player {player_from_team_1+1} plays with Hand: {player_1_choose}')
    print(f'Team2: Player {player_from_team_2+1} plays with Hand: {player_2_choose}')
    result = find_round_winner(player_1_choose, player_2_choose)
    report_winner(result)

    if result == 1:
        team_1[player_from_team_1] += 1
    elif result == 2:
        team_2[player_from_team_2] += 1
    print('Update Team Stats:')
    print_two_team_stat(team_1, team_2)
    print()


def play_all_rounds(round_count: int,
                    team_1: list[int],
                    team_2: list[int]) -> None:
    '''This function Repetitively  for round_count rounds.'''
    for i in range(1, round_count+1):
        print(f'Round{i}:')
        play_one_round(team_1, team_2)


def find_final_winner(team_1: list[int], team_2: list[int]) -> tuple:
    '''This function will calculate the winner it will return
    (number of winning team, number of win,
    number of win of other team) respectively'''
    score_team_1 = sum(team_1)
    score_team_2 = sum(team_2)

    if score_team_1 == score_team_2:
        return 0, score_team_1, score_team_2
    elif score_team_1 > score_team_2:
        return 1, score_team_1, score_team_2
    else:
        return 2, score_team_2, score_team_1


def main() -> None:
    '''This function run a entire program'''

    Player_count = int(input('Enter number of players: '))
    round_count = int(input('Enter number of rounds: '))
    team_1 = initialize_list(Player_count)
    team_2 = initialize_list(Player_count)

    print('Initial Team Stats:')
    print_two_team_stat(team_1, team_2)
    print('Playing...')
    play_all_rounds(round_count, team_1, team_2)
    print('Game over...')

    result, win_score, lose_score = find_final_winner(team_1, team_2)

    if result:
        print(f'Team {result} wins.')
    else:
        print('Both teams tie.')

    print(f'Final scores: {win_score} vs. {lose_score}')


if __name__ == '__main__':
    main()
