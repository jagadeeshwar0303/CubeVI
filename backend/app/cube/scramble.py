"""Scramble generation for demos and repeatable experiments."""

import random

from app.cube.moves import FACE_PERMUTATIONS, MOVE_SUFFIXES, apply_sequence
from app.cube.state import CubeState


def generate_scramble(length: int = 6, seed: int | None = None) -> tuple[list[str], CubeState]:
    """Return a random move list and the state produced by applying it."""
    # TODO: use random.Random(seed), avoid repeating a face, and call
    # apply_sequence(CubeState.solved(), moves).
    raise NotImplementedError

