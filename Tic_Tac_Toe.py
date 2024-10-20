def print_board(board):
    print("\n")
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("---+---+---")
    print("\n")


def find_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None


def tic_tac_toe():
    print("Welcome to TicTacToe!\n")
    print("Player 1: X")
    print("Player 2: O\n")
    print("Enter your move as 'row column' (e.g., '1 1' for center).\n")

    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        player = "X"
        for _ in range(9):
            print_board(board)
            print(f"Player {player}'s turn")

            while True:
                move = input("Enter row and column (0, 1, or 2): ").split()
                if len(move) != 2 or not all(i.isdigit() for i in move):
                    print("Invalid input! Please enter two numbers separated by a space.")
                    continue

                row, col = map(int, move)
                if row not in range(3) or col not in range(3):
                    print("Invalid move! Row and column must be 0, 1, or 2.")
                elif board[row][col] != " ":
                    print("Invalid move! The cell is already taken.")
                else:
                    break

            board[row][col] = player
            winner = find_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break

            player = "O" if player == "X" else "X"
        else:
            print_board(board)
            print("It's a tie!")

        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            break


tic_tac_toe()
