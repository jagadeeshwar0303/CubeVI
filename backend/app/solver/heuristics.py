"""Heuristic functions for informed search."""

from app.cube.state import CubeState

def heuristic(state: CubeState) -> int:
    misplaced = sum(
        state.cp[i] != i for i in range(8)
    )

    return  (misplaced + 3) // 4