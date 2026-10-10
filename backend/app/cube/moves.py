from app.cube.state import CubeState

# Old sticker index -> new sticker index. Baseline move families: U, R, F.
FACE_PERMUTATIONS = {
    "U": (1, 3, 0, 2, 20, 21, 6, 7, 4, 5, 10, 11, 12, 13, 14, 15, 8, 9, 18, 19, 16, 17, 22, 23),
    "R": (0, 9, 2, 11, 5, 7, 4, 6, 8, 13, 10, 15, 12, 22, 14, 20, 16, 17, 18, 19, 1, 21, 3, 23),
    "F": (0, 1, 4, 6, 12, 5, 13, 7, 9, 11, 8, 10, 17, 19, 14, 15, 16, 2, 18, 3, 20, 21, 22, 23),
}
MOVE_SUFFIXES = ("", "'", "2")

def normalize_move(move):
    move = move.strip().upper()
    if not move or move[0] not in FACE_PERMUTATIONS or move[1:] not in MOVE_SUFFIXES:
        raise ValueError(f"Unsupported move: {move}")
    return move

def apply_move(cube, move):
    move = normalize_move(move)
    turns = 2 if move.endswith("2") else 3 if move.endswith("'") else 1
    current = cube
    for _ in range(turns):
        values = [""] * 24
        for old, new in enumerate(FACE_PERMUTATIONS[move[0]]):
            values[new] = current.stickers[old]
        current = CubeState(tuple(values))
    return current

def apply_sequence(cube, moves):
    for move in moves:
        cube = apply_move(cube, move)
    return cube

def inverse_move(move):
    move = normalize_move(move)
    return move if move.endswith("2") else move[0] if move.endswith("'") else move + "'"

def inverse_sequence(moves):
    return [inverse_move(move) for move in reversed(moves)]

