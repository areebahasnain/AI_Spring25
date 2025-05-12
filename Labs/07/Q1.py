import copy
import math

# Constants
EMPTY = '.'
WHITE = 'w'
BLACK = 'b'

BOARD_SIZE = 8

DIRECTIONS = {
    WHITE: [(-1, -1), (-1, 1)],
    BLACK: [(1, -1), (1, 1)]
}

def initialize_board():
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if (x + y) % 2 == 1:
                if y < 3:
                    board[y][x] = BLACK
                elif y > 4:
                    board[y][x] = WHITE
    return board

def print_board(board):
    print("  " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for y in range(BOARD_SIZE):
        print(y, " ".join(board[y]))
    print()

def in_bounds(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

def get_valid_moves(board, x, y):
    piece = board[y][x]
    if piece == EMPTY:
        return []

    moves = []
    captures = []
    for dy, dx in DIRECTIONS[piece]:
        nx, ny = x + dx, y + dy
        if in_bounds(nx, ny) and board[ny][nx] == EMPTY:
            moves.append(((x, y), (nx, ny)))
        elif in_bounds(nx, ny) and board[ny][nx].lower() != piece.lower() and board[ny][nx] != EMPTY:
            cx, cy = nx + dx, ny + dy
            if in_bounds(cx, cy) and board[cy][cx] == EMPTY:
                captures.append(((x, y), (cx, cy)))
    return captures if captures else moves

def get_all_moves(board, player):
    moves = []
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[y][x] == player:
                moves.extend(get_valid_moves(board, x, y))
    return moves

def make_move(board, move):
    (x1, y1), (x2, y2) = move
    new_board = copy.deepcopy(board)
    piece = new_board[y1][x1]
    new_board[y1][x1] = EMPTY
    new_board[y2][x2] = piece

    # Check for capture
    if abs(x2 - x1) == 2:
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2
        new_board[my][mx] = EMPTY
    return new_board

def evaluate(board):
    """Basic evaluation: difference in piece count"""
    w = sum(row.count(WHITE) for row in board)
    b = sum(row.count(BLACK) for row in board)
    return b - w  # Maximize for AI (Black)

def minimax(board, depth, alpha, beta, maximizing_player):
    current_player = BLACK if maximizing_player else WHITE
    moves = get_all_moves(board, current_player)

    if depth == 0 or not moves:
        return evaluate(board), None

    best_move = None

    if maximizing_player:
        max_eval = -math.inf
        for move in moves:
            new_board = make_move(board, move)
            eval_score, _ = minimax(new_board, depth - 1, alpha, beta, False)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in moves:
            new_board = make_move(board, move)
            eval_score, _ = minimax(new_board, depth - 1, alpha, beta, True)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_move

def is_game_over(board):
    return not get_all_moves(board, WHITE) or not get_all_moves(board, BLACK)

board = initialize_board()
print_board(board)

while not is_game_over(board):
    # Human (White)
    human_moves = get_all_moves(board, WHITE)
    if not human_moves:
        print("You have no valid moves. You lose!")
        break

    print("Your turn (White):")
    while True:
        try:
            from_x = int(input("From X: "))
            from_y = int(input("From Y: "))
            to_x = int(input("To X: "))
            to_y = int(input("To Y: "))
            move = ((from_x, from_y), (to_x, to_y))
            if move in human_moves:
                board = make_move(board, move)
                print_board(board)
                break
            else:
                print("Invalid move. Try again.")
        except Exception:
            print("Invalid input. Enter numbers.")

    if is_game_over(board):
        break

    # AI (Black)
    print("AI's turn (Black)...")
    _, ai_move = minimax(board, 4, -math.inf, math.inf, True)
    if ai_move:
        print(f"AI moves: {ai_move[0]} → {ai_move[1]}")
        board = make_move(board, ai_move)
        print_board(board)
    else:
        print("AI has no moves. You win!")
        break

print("Game Over!")
w = sum(row.count(WHITE) for row in board)
b = sum(row.count(BLACK) for row in board)
if w > b:
    print("You win!")
elif b > w:
    print("AI wins!")
else:
    print("It's a draw!")


