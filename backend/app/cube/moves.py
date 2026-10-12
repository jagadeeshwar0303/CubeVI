"""Move notation and state transitions.

Learning goal: encode each face turn as a permutation. Search code should call
apply_move() rather than knowing sticker indexes itself.
"""

from app.cube.state import CubeState

FACE_PERMUTATIONS: dict[str, tuple[int, ...]] = {
    # TODO: replace each empty tuple with a verified old-index -> new-index map.
    "U": (), "R": (), "F": (), "D": (), "L": (), "B": (),
}
MOVE_SUFFIXES = ("", "'", "2")


def normalize_move(move: str) -> str:
    """Validate notation such as R, R', or R2 and return canonical text."""
    # TODO: uppercase the face, preserve suffix, and raise ValueError for bad input.
    raise NotImplementedError


def apply_move(cube: CubeState, move: str) -> CubeState:
    """Return a new state after one face move without mutating cube."""
    # TODO: use the permutation once, twice, or three times for normal, half,
    # and inverse turns respectively.
    raise NotImplementedError


def apply_sequence(cube: CubeState, moves: list[str]) -> CubeState:
    """Apply a scramble or solution from left to right."""
    # TODO: repeatedly call apply_move and return the final state.
    raise NotImplementedError


def inverse_move(move: str) -> str:
    """Return the notation that reverses one move."""
    # TODO: R <-> R' and R2 -> R2.
    raise NotImplementedError


def inverse_sequence(moves: list[str]) -> list[str]:
    """Reverse a sequence and invert every move."""
    # TODO: reverse the list, then call inverse_move on each item.
    raise NotImplementedError

