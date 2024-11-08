def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    """Use backtracking to place queens on the board starting from the given column."""
    if col >= len(board):
        return True  

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  

            if solve_n_queens(board, col + 1):  
                return True

            board[i][col] = 0  

    return False  

def print_board(board):
    """Print the chessboard with queens."""
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print()

def solve_n_queens_interactive():
    """Function to solve the N-Queens problem interactively."""
    try:
        n = int(input("Enter the size of the chessboard (N for N-Queens): "))
        if n < 1:
            print("The board size must be at least 1.")
            return
        
        board = [[0 for _ in range(n)] for _ in range(n)]
        
        if solve_n_queens(board, 0):  
            print(f"Solution for {n}-Queens:")
            print_board(board)
        else:
            print(f"No solution exists for {n}-Queens.")
    except ValueError:
        print("Invalid input! Please enter a positive integer.")

if __name__ == "__main__":
    solve_n_queens_interactive()
