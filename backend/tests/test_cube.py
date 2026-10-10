from app.cube.moves import apply_sequence, inverse_sequence
from app.cube.state import CubeState

def test_inverse_sequence_restores_state():
    scramble = ["R", "U'", "F2"]
    cube = apply_sequence(CubeState.solved(), scramble)
    assert apply_sequence(cube, inverse_sequence(scramble)) == CubeState.solved()

