def print_board(board):
    # Function to print the Tic-Tac-Toe board
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board):
    # Function to check if there's a winner
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def is_full(board):
    # Function to check if the board is full
    return " " not in board

def main():
    board = [" "] * 9  # A list to represent the Tic-Tac-Toe board
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        move = -1

        while move < 1 or move > 9 or board[move - 1] != " ":
            try:
                move = int(input(f"Player {current_player}, enter your move (1-9): "))
            except ValueError:
                pass  # Handle invalid input
            if move < 1 or move > 9 or board[move - 1] != " ":
                print("This spot is already taken or invalid. Try again.")
        
        board[move - 1] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            game_over = True
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"  # Switch players

        if game_over:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                main()  # Restart the game

if __name__ == "__main__":
    main()
