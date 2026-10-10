from dataclasses import dataclass
from app.solver.search import breadth_first_search

@dataclass(frozen=True)
class SolveResult:
    moves: list[str]
    explanation: str

def solve(cube, constraint):
    if cube.is_solved():
        return SolveResult([], "The cube is already solved.")
    depth = int(constraint["value"]) if constraint.get("type") == "max_moves" else 8
    moves = breadth_first_search(cube, depth)
    return None if moves is None else SolveResult(moves, f"Breadth-first search found a solution in {len(moves)} moves.")

