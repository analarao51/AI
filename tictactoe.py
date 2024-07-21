def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2-i] == player for i in range(3)]):
        return True
    
    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == '_':
                return False
    return True

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def tic_tac_toe(moves):
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    player = 'X'
    
    for move in moves:
        row, col = move
        if board[row][col] == '_':
            board[row][col] = player
        else:
            raise ValueError("Invalid move")
        
        if check_winner(board, player):
            return player
        
        player = 'O' if player == 'X' else 'X'
    
    if check_draw(board):
        return "Draw"
    
    return "Pending"

# Test example
moves = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (1, 0), (1, 2), (2, 2), (2, 1)]
result = tic_tac_toe(moves)
print(result)  # Output: "Draw"
