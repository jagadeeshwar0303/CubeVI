"""Validation functions kept separate from the state data model."""

from app.cube.state import CubeState


def validate_cube(faces: dict[str, list[str]]) -> tuple[bool, str]:
    """Return a friendly validation result for an input form."""
    # TODO: call CubeState.from_faces() and translate ValueError to (False, message).
    raise NotImplementedError


def validate_solvability(cube: CubeState) -> tuple[bool, str]:
    """Check whether a colour arrangement can exist on a physical cube."""
    # TODO: add corner permutation/orientation checks after the cubie model is stable.
    raise NotImplementedError

