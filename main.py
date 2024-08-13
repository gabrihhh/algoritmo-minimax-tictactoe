import os

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 

def print_board(board):
    os.system('clear')
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')

def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  
                      (0, 4, 8), (2, 4, 6)]             
    return any(board[i] == board[j] == board[k] == player for i, j, k in win_conditions)

def is_board_full(board):
    return ' ' not in board

def evaluate(board):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 1 or score == -1:
        return score

    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best_score = max(best_score, minimax(board, depth + 1, False))
                board[i] = ' ' 

        return best_score

    else:
        best_score = float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best_score = min(best_score, minimax(board, depth + 1, True))
                board[i] = ' ' 

        return best_score

def find_best_move(board):
    best_move = -1
    best_value = -float('inf')

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_value = minimax(board, 0, False)
            board[i] = ' '

            if move_value > best_value:
                best_value = move_value
                best_move = i

    return best_move

def play_game():
    board = [' ' for _ in range(9)]
    player_turn = 'O' 

    while True:
        print_board(board)

        if player_turn == 'O':
            move = int(input("Escolha sua jogada (1-9): "))-1
            if board[move] == ' ':
                board[move] = 'O'
                player_turn = 'X'
        else: 
            move = find_best_move(board)
            board[move] = 'X'
            player_turn = 'O'

        if check_winner(board, 'X'):
            print("O computador venceu!")
            break
        elif check_winner(board, 'O'):
            print("Você venceu!")
            break
        elif is_board_full(board):
            print("Empate!")
            break

    print_board(board)

play_game()
