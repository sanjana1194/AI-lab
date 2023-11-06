import random

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)

def check_winner(player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(all(board[i] == player for i in combo) for combo in winning_combinations)

def player_move():
    move = int(input(f"Player X, enter a position (1-9): ")) - 1
    return move

def computer_move():
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(empty_cells) if empty_cells else None

current_player = "X"
while True:
    print_board()
    
    move = player_move() if current_player == "X" else computer_move()

    if move is not None and board[move] == " ":
        board[move] = current_player
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif " " not in board:
            print_board()
            print("It's a tie!")
            break
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Invalid move. Try again.")
