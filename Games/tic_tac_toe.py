print("Welcome to Tic-Tac-Toe!")

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def display_board():
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def player_move(player):
    while True:
        choice = input(f"Player {player}, enter position (1-9): ")
        if choice in "123456789" and board[int(choice) - 1] not in ["X", "O"]:
            board[int(choice) - 1] = player
            break
        print("Invalid move! Try again.")

def check_win():
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return True
    return False

display_board()
player_move("X")
display_board()
