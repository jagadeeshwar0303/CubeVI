"""Tests that define the cube-engine contract before implementation."""

import pytest


@pytest.mark.skip(reason="Implement CubeState and move permutations first")
def test_solved_cube_is_solved():
    """The canonical solved state must report solved."""
    # TODO: import CubeState and assert CubeState.solved().is_solved().
    assert True


@pytest.mark.skip(reason="Implement CubeState and move permutations first")
def test_move_and_inverse_restore_state():
    """A move followed by its inverse must return the original state."""
    # TODO: apply U then U' and compare state keys.
    assert True

