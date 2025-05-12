import random
from collections import deque
from typing import Deque

GAME_SIZE = 6

def alphabeta(
    state: Deque[int],
    alpha: float = float('-inf'),
    beta: float = float('inf'),
    maximizing: bool = True,
    max_score: int = 0,
    min_score: int = 0
):
    if not state:
        return max_score - min_score, None
    
    best_move = None
    if maximizing:
        max_val = float('-inf')

        left = state.popleft()
        v, _ = alphabeta(state, alpha, beta, False, max_score + left, min_score)
        state.appendleft(left)

        if v > max_val:
            max_val = v
            best_move = 0
        alpha = max(alpha, v)
        if beta <= alpha:
            return max_val, best_move
        
        right = state.pop()
        v, _ = alphabeta(state, alpha, beta, False, max_score + right, min_score)
        state.append(right)

        if v > max_val:
            max_val = v
            best_move = -1
        return max_val, best_move
    else:
        min_val = float('inf')

        left = state.popleft()
        v, _ = alphabeta(state, alpha, beta, True, max_score, min_score + left)
        state.appendleft(left)

        if v < min_val:
            min_val = v
            best_move = 0
        beta = min(beta, v)
        if beta <= alpha:
            return min_val, best_move
        
        right = state.pop()
        v, _ = alphabeta(state, alpha, beta, True, max_score, min_score + right)
        state.append(right)

        if v < min_val:
            min_val = v
            best_move = -1
        return min_val, best_move

game = deque(random.randrange(1, GAME_SIZE) for _ in range(GAME_SIZE))
str_cards = lambda: f"[{", ".join(map(str, game))}]"
print("Initial Cards:", str_cards())

max_score = min_score = 0
while True:
    max_idx = alphabeta(game)[1]
    max_pick = game[max_idx]
    max_score += max_pick
    del game[max_idx]

    print(f"Max picks {max_pick}, Remaining Cards: {str_cards()}")
    if not game:
        break

    min_idx = min(range(len(game)), key=game.__getitem__)
    min_pick = game[min_idx]
    min_score += min_pick
    del game[min_idx]

    print(f"Min picks {min_pick}, Remaining Cards: {str_cards()}")
    if not game:
        break
    
print(f"Final Scores - Max: {max_score}, Min: {min_score}")
print("Winner:", "Max" if max_score > min_score else "Draw" if max_score == min_score else "Min")
