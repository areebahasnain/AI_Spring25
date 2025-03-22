class SimpleChessBoard:
    """
    A simplified chess board representation with basic move generation and evaluation
    """

    EMPTY = 0
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

    # Piece values for simple evaluation
    PIECE_VALUES = {
        EMPTY: 0,
        PAWN: 100,
        KNIGHT: 320,
        BISHOP: 330,
        ROOK: 500,
        QUEEN: 900,
        KING: 20000
    }

    def __init__(self):
        # Initialize an 8x8 board
        # Positive numbers for white pieces, negative for black
        self.board = [
            [-4, -2, -3, -5, -6, -3, -2, -4],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [4, 2, 3, 5, 6, 3, 2, 4]
        ]
        self.white_to_move = True
        self.move_history = []

    def copy(self):
        """Create a deep copy of the board"""
        new_board = SimpleChessBoard()
        new_board.board = [row[:] for row in self.board]
        new_board.white_to_move = self.white_to_move
        new_board.move_history = self.move_history.copy()
        return new_board

    def get_piece_type(self, piece):
        """Get piece type regardless of color"""
        return abs(piece)

    def is_white_piece(self, piece):
        """Check if piece is white"""
        return piece > 0

    def is_black_piece(self, piece):
        """Check if piece is black"""
        return piece < 0

    def get_simple_legal_moves(self):
        """
        Generate simplified legal moves
        Returns a list of moves in format: [(from_row, from_col, to_row, to_col), ...]
        """
        moves = []

        # For each square on the board
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]

                # Skip empty squares or opponent pieces
                if piece == 0 or (self.white_to_move and piece < 0) or (not self.white_to_move and piece > 0):
                    continue

                piece_type = self.get_piece_type(piece)

                # Generate pawn moves
                if piece_type == self.PAWN:
                    self._add_pawn_moves(r, c, moves)

                # Generate knight moves
                elif piece_type == self.KNIGHT:
                    self._add_knight_moves(r, c, moves)

                # Simple moves for other pieces (simplified for demo)
                # In a full implementation, you would add proper move generation for each piece type
                else:
                    # Just generate some placeholder moves for demonstration
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue

                            new_r, new_c = r + dr, c + dc
                            if 0 <= new_r < 8 and 0 <= new_c < 8:
                                target = self.board[new_r][new_c]
                                if target == 0 or (self.white_to_move and target < 0) or (
                                        not self.white_to_move and target > 0):
                                    moves.append((r, c, new_r, new_c))

        return moves

    def _add_pawn_moves(self, r, c, moves):
        """Generate pawn moves"""
        direction = -1 if self.white_to_move else 1  # White pawns move up (decreasing row), black down

        # Forward move
        new_r = r + direction
        if 0 <= new_r < 8 and self.board[new_r][c] == 0:
            moves.append((r, c, new_r, c))

            # Double move from starting position
            starting_row = 6 if self.white_to_move else 1
            if r == starting_row:
                new_r = r + 2 * direction
                if 0 <= new_r < 8 and self.board[new_r][c] == 0:
                    moves.append((r, c, new_r, c))

        # Capture moves
        for dc in [-1, 1]:
            new_c = c + dc
            if 0 <= new_r < 8 and 0 <= new_c < 8:
                target = self.board[new_r][new_c]
                if (self.white_to_move and target < 0) or (not self.white_to_move and target > 0):
                    moves.append((r, c, new_r, new_c))

    def _add_knight_moves(self, r, c, moves):
        """Generate knight moves"""
        knight_moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]

        for dr, dc in knight_moves:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < 8 and 0 <= new_c < 8:
                target = self.board[new_r][new_c]
                if target == 0 or (self.white_to_move and target < 0) or (not self.white_to_move and target > 0):
                    moves.append((r, c, new_r, new_c))

    def make_move(self, move):
        """Apply a move to the board"""
        from_row, from_col, to_row, to_col = move

        # Store move in history
        self.move_history.append((move, self.board[to_row][to_col]))

        # Move piece
        self.board[to_row][to_col] = self.board[from_row][from_col]
        self.board[from_row][from_col] = 0

        # Switch turn
        self.white_to_move = not self.white_to_move

    def undo_move(self):
        """Undo the last move"""
        if not self.move_history:
            return

        move, captured = self.move_history.pop()
        from_row, from_col, to_row, to_col = move

        # Restore piece to original position
        self.board[from_row][from_col] = self.board[to_row][to_col]
        self.board[to_row][to_col] = captured

        # Switch turn back
        self.white_to_move = not self.white_to_move

    def evaluate(self):
        """
        Simple evaluation function based on material balance
        Positive scores favor white, negative favor black
        """
        score = 0

        # Material value
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece > 0:  # White piece
                    score += self.PIECE_VALUES[piece]
                elif piece < 0:  # Black piece
                    score -= self.PIECE_VALUES[-piece]

        # Add some positional bonus (simplified)
        # Center control bonus
        center_squares = [(3, 3), (3, 4), (4, 3), (4, 4)]
        for r, c in center_squares:
            piece = self.board[r][c]
            if piece > 0:  # White piece
                score += 10
            elif piece < 0:  # Black piece
                score -= 10

        return score if self.white_to_move else -score

    def move_to_algebraic(self, move):
        """Convert a move to algebraic notation"""
        from_row, from_col, to_row, to_col = move
        cols = "abcdefgh"
        rows = "87654321"  # Inverted because chess notation starts from bottom
        return f"{cols[from_col]}{rows[from_row]}{cols[to_col]}{rows[to_row]}"

    def __str__(self):
        """String representation of the board"""
        piece_symbols = {
            0: ".",
            1: "P", -1: "p",
            2: "N", -2: "n",
            3: "B", -3: "b",
            4: "R", -4: "r",
            5: "Q", -5: "q",
            6: "K", -6: "k"
        }

        s = "  a b c d e f g h\n"
        for r in range(8):
            s += f"{8 - r} "
            for c in range(8):
                s += piece_symbols[self.board[r][c]] + " "
            s += f"{8 - r}\n"
        s += "  a b c d e f g h"
        return s


def beam_search_chess(board, beam_width, depth_limit):
    """
    Perform beam search to find the best move

    Args:
        board: SimpleChessBoard instance
        beam_width: Number of promising paths to keep at each level
        depth_limit: Maximum search depth

    Returns:
        best_move: Best move found
        best_score: Evaluation score of the best move
    """
    # Base case: reached depth limit
    if depth_limit == 0:
        return None, board.evaluate()

    legal_moves = board.get_simple_legal_moves()
    if not legal_moves:
        # No legal moves (simplified - in a real chess engine this would be checkmate or stalemate)
        return None, board.evaluate()

    # Evaluate all immediate moves
    candidates = []
    for move in legal_moves:
        new_board = board.copy()
        new_board.make_move(move)
        score = new_board.evaluate()
        candidates.append((move, score, new_board))

    # Sort moves by score (highest first for white, lowest first for black)
    candidates.sort(key=lambda x: x[1], reverse=board.white_to_move)

    # Keep only the top beam_width candidates
    candidates = candidates[:beam_width]

    if depth_limit == 1:
        # If we're at the last level, just return the best move
        return candidates[0][0], candidates[0][1]

    best_move = None
    best_score = float('-inf') if board.white_to_move else float('inf')

    # Recursively search each candidate
    for move, _, new_board in candidates:
        _, sub_score = beam_search_chess(new_board, beam_width, depth_limit - 1)

        # Update best move if this path is better
        if (board.white_to_move and sub_score > best_score) or \
                (not board.white_to_move and sub_score < best_score):
            best_score = sub_score
            best_move = move

    return best_move, best_score



# Create a new chess board (standard starting position)
board = SimpleChessBoard()

# Print the initial board
print("Initial board:")
print(board)
print()

# Find the best move using beam search
beam_width = 3  # Consider top 3 moves at each level
depth_limit = 3  # Look 3 moves ahead

best_move, score = beam_search_chess(board, beam_width, depth_limit)

# Print the result
if best_move:
    from_row, from_col, to_row, to_col = best_move
    algebraic = board.move_to_algebraic(best_move)
    piece = board.board[from_row][from_col]
    piece_type = board.get_piece_type(piece)
    piece_names = {
        1: "Pawn", 2: "Knight", 3: "Bishop",
        4: "Rook", 5: "Queen", 6: "King"
    }

    print(f"Best move: {piece_names[piece_type]} from {algebraic[:2]} to {algebraic[2:]} (score: {score})")
else:
    print("No valid move found")


