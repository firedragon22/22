def is_win(game):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        # Check rows and columns
        if game[i][0] == game[i][1] == game[i][2] != ' ':
            return True
        if game[0][i] == game[1][i] == game[2][i] != ' ':
            return True
    
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] != ' ':
        return True
    if game[0][2] == game[1][1] == game[2][0] != ' ':
        return True
    
    return False

def print_board(game):
    # Display the game board
    for row in game:
        print(" | ".join(row))
        print("-" * 5)

def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1 = 'X'
    player2 = 'O'
    turn = False  # False for player 1's turn, True for player 2's turn. Player 1 first.
    
    print("X = Player 1")
    print("O = Player 2")
    
    for n in range(9):
        print_board(game)
        if not turn:
            print("Player 1's turn")
        else:
            print("Player 2's turn")
        
        # Input validation loop
        while True:
            try:
                print("Enter row and column (1-3): ", end="")
                i, j = map(int, input().split())
                i -= 1  # Convert to 0-indexed
                j -= 1  # Convert to 0-indexed
                if game[i][j] == ' ':
                    break  # Valid input
                else:
                    print("Cell is already taken, try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column between 1 and 3.")
        
        # Mark the board
        if not turn:
            game[i][j] = 'X'
        else:
            game[i][j] = 'O'
        
        # Check for a winner
        if is_win(game):
            print_board(game)
            print("Player", 1 if not turn else 2, "wins!")
            break  # End the game
        
        # Check for a tie after 9 turns
        if n == 8:
            print_board(game)
            print("It's a tie!")
        
        turn = not turn  # Switch turns

if __name__ == "__main__":
    main()
