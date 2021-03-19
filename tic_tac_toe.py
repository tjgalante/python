'''
Simple Tic Tac Toe game (Milestone Project 1) from the
2021 Complete Python Bootcamp on Udemy
NOTE: Does not use exception handling, as it was not covered at this point
'''

from os import system, name
import random

def clear_output():
    '''Clear screen between plays'''
    # for Windows
    if name == 'nt':
        _ = system('cls')

    # for Mac and Linux
    else:
        _ = system('clear')

def display_board(board):
    '''Print game board'''
    clear_output()
    print('   |   |    ')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print('   |   |    ')
    print('-----------')
    print('   |   |    ')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('   |   |    ')
    print('-----------')
    print('   |   |    ')
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('   |   |    ')
    print('')

def player_input():
    '''Ask player which character he/she would like to use'''
    valid = False
    markers = ('X', 'O')

    while not valid:
        mark = (input("Please pick a marker 'X' or 'O': ").upper())
        valid = mark in markers

        if not valid:
            print("Invalid input")

    return mark

def place_marker(board, marker, position):
    '''Mark position on board with X or O'''
    board[position-1] = marker

def win_check(board, mark):
    '''Check if there is a winning line'''
    # check horizontal lines
    for idx in range(0, 6, 3):
        if board[idx] == mark and board[idx+1] == mark and board[idx+2] == mark:
            return True
    # check vertical lines
    for idx in range(0, 3):
        if board[idx] == mark and board[idx+3] == mark and board[idx+6] == mark:
            return True
    # check diagonals
    if board[4] == mark and ((board[0] == mark and board[8] == mark) or \
            (board[2] == mark and board[6] == mark)):
        return True
    return False

def choose_first():
    '''Randomly choose if player1 is an X or an O'''
    return random.randint(1, 2)

def space_check(board, position):
    '''Check if space is already occupied by an X or O'''
    return board[position] == ' '

def full_board_check(board):
    '''Check for empty board spaces'''
    if ' ' in board:
        return False
    return True

def player_choice(board):
    '''Get valid space from player'''
    position = -1
    while True:
        pos = input('Choose a square: ')
        if not pos.isdigit():
            print('Please enter a digit between 1 and 9')
        else:
            position = int(pos)
            if position not in range(1, 10):
                print('Please enter a digit between 1 and 9')
            else:
                if not space_check(board, position-1):
                    print('Square is already taken. Please try again')
                else:
                    break
    return position - 1

def replay():
    '''At end of game, ask if user would like to play again'''
    valid = False
    values = ('Y', 'N')

    while not valid:
        response = (input("Do you want to play again? 'Y' or 'N' ").upper())
        valid = response in values

        if not valid:
            print("Invalid input")
        else:
            result = response == 'Y'

    return result

# Start of game
print('Welcome to Tic Tac Toe!')

while True:
    game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    players = {}

    display_board(game_board)

    current_player = choose_first()
    print(f'Player {current_player} goes first')

    players[current_player] = player_input()
    next_player = (current_player % 2) + 1

    if players[current_player] == 'X':
        players[next_player] = 'O'
    else:
        players[next_player] = 'X'

    while True:
        print(f'Player {current_player} ({players[current_player]})')
        chosen_position = player_choice(game_board)
        game_board[chosen_position] = players[current_player]
        display_board(game_board)

        if win_check(game_board, players[current_player]):
            print(f'Player {current_player} ({players[current_player]}) wins!')
            break

        if full_board_check(game_board):
            print('Cat game, it\'s a tie!')
            break

        current_player = (current_player % 2) + 1

    if not replay():
        break
