import random

# Define the Tic-Tac-Toe board
board = [' ' for _ in range(9)]


# Function to display the Tic-Tac-Toe board
def display_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])


# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board


# Function to check if a player has won
def check_winner(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


# Function for the AI to make a move
def ai_move(board):
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


# Minimax algorithm for AI
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score


# Main game loop
def play_game():
    while True:
        display_board(board)

        if not is_board_full(board):
            player_move = int(input("Enter your move (1-9): ")) - 1

            if 0 <= player_move < 9 and board[player_move] == ' ':
                board[player_move] = 'X'
            else:
                print("Invalid move. Try again.")
                continue
        else:
            print("It's a draw!")
            break

        if check_winner(board, 'X'):
            display_board(board)
            print("You win!")
            break

        if not is_board_full(board):
            ai = ai_move(board)
            board[ai] = 'O'
        else:
            print("It's a draw!")
            break

        if check_winner(board, 'O'):
            display_board(board)
            print("AI wins!")
            break


# Start the game
play_game()
