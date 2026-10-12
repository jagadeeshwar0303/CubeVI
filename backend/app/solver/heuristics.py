"""Heuristic functions for informed search."""

from app.cube.state import CubeState


def misplaced_stickers(cube: CubeState) -> int:
    """Count stickers that differ from the solved reference."""
    # TODO: implement this first as an educational progress signal.
    raise NotImplementedError


def lower_bound(cube: CubeState) -> int:
    """Return a safe estimate used by IDA* threshold calculations."""
    # TODO: begin conservatively, then improve using corner orientation and
    # permutation tables. Explain why the bound must not overestimate.
    raise NotImplementedError

