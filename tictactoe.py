# Create Board
def create_board():
    board = []
    for i in range(9):
        board.append(i)

    return board


# Display Board (3x3 grid of list)
def display_board(board):
    for i in range(0, 9, 3):  # range(start, stop, step)
        print(board[i], board[i + 1], board[i + 2])


# Get Player Move (Handle human player's turn)
def get_player_move(board):
    player_move = input("Make Your Move:")
    player_response = int(player_move)

    return player_response


# Get Bot Move

# Validate Move

# Make Move (Update Board)

# Check Winner

# Check Draw

# Play Game
## board[player_response] = "X"
## display_board(board)


def main():
    board = create_board()
    display_board(board)
    player_response = get_player_move(board)


if __name__ == "__main__":
    main()
