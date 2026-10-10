from app.cube.moves import apply_move
from app.cube.state import CubeState
from app.solver.search import breadth_first_search

def test_solver_solves_one_move():
    assert breadth_first_search(apply_move(CubeState.solved(), "U"), 2) == ["U'"]

