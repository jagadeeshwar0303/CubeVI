from collections import deque
from app.cube.moves import FACE_PERMUTATIONS, MOVE_SUFFIXES, apply_move

def breadth_first_search(start, max_depth=8):
    if start.is_solved():
        return []
    queue = deque([(start, [])])
    visited = {start.stickers}
    while queue:
        state, path = queue.popleft()
        if len(path) >= max_depth:
            continue
        for face in FACE_PERMUTATIONS:
            for suffix in MOVE_SUFFIXES:
                move = face + suffix
                next_state = apply_move(state, move)
                next_path = path + [move]
                if next_state.is_solved():
                    return next_path
                if next_state.stickers not in visited:
                    visited.add(next_state.stickers)
                    queue.append((next_state, next_path))
    return None

