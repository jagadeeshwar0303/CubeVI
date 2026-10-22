"""Scramble generation for demos and repeatable experiments."""

import random
from .moves import apply_move
from .state import CubeState

ALL_MOVES = [
    "U", "U'", "U2",
    "D", "D'", "D2",
    "R", "R'", "R2",
    "L", "L'", "L2",
    "F", "F'", "F2",
    "B", "B'", "B2",
]

def generate_scramble(length: int = 20):
    """ Generate a valid random 2x2x2 cube state 
        length : number of random moves to apply """

    if length < 0 : 
        raise ValueError("Scramble length cannot be negative")

    state = CubeState()
    scramble_moves = []

    previous_face = None

    for _ in range(length):

        # Avoid consecutive turns of the same face.
        possible_moves = [
            move for move in ALL_MOVES 
            if move[0] != previous_face
        ]

        move = random.choice(possible_moves)

        state = apply_move(state, move)
        scramble_moves.append(move)
        previous_face = move[0]

    return state, scramble_moves




    

