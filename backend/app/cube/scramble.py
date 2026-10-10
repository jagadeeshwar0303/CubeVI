import random
from app.cube.moves import FACE_PERMUTATIONS, MOVE_SUFFIXES, apply_sequence
from app.cube.state import CubeState

def generate_scramble(length=6, seed=None):
    rng = random.Random(seed)
    moves, previous = [], ""
    while len(moves) < length:
        face = rng.choice(tuple(FACE_PERMUTATIONS))
        if face == previous:
            continue
        moves.append(face + rng.choice(MOVE_SUFFIXES))
        previous = face
    return moves, apply_sequence(CubeState.solved(), moves)

