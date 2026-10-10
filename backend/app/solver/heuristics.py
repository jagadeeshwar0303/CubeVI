from app.cube.state import CubeState

def misplaced_stickers(cube):
    solved = CubeState.solved()
    return sum(a != b for a, b in zip(cube.stickers, solved.stickers))

def lower_bound(cube):
    return 0 if cube.is_solved() else 1

