"""Core data model for a 2x2x2 cube.

Learning goal: keep the cube state independent from FastAPI, React, and the
search algorithm. Every other layer should ask this module to read or change
the cube instead of manipulating raw lists directly.
"""

from dataclasses import dataclass

FACES = ("U", "R", "F", "D", "L", "B")
COLOURS = frozenset({"W", "R", "G", "Y", "O", "B"})
STICKERS_PER_FACE = 4


@dataclass(frozen=True)
class CubeState:
    """Immutable cube snapshot stored as 24 stickers."""

    stickers: tuple[str, ...]

    @classmethod
    def solved(cls) -> "CubeState":
        """Return the solved cube used by tests and scramble generation."""
        # TODO: construct one block of four stickers for every face in FACES.
        raise NotImplementedError

    @classmethod
    def from_faces(cls, faces: dict[str, list[str]]) -> "CubeState":
        """Convert six UI face arrays into one validated internal state."""
        # TODO: validate face names, lengths, legal colours, and four occurrences
        # of every colour before constructing the immutable tuple.
        raise NotImplementedError

    def to_faces(self) -> dict[str, list[str]]:
        """Convert the internal tuple back to the shape expected by the UI."""
        # TODO: slice four stickers at a time and map each slice to FACES.
        raise NotImplementedError

    def is_solved(self) -> bool:
        """Tell the solver whether every face contains one uniform colour."""
        # TODO: check every group of four stickers, not only colour counts.
        raise NotImplementedError

    def key(self) -> tuple[str, ...]:
        """Return the hashable identity used by visited-state search sets."""
        # TODO: return the canonical tuple representation.
        raise NotImplementedError

