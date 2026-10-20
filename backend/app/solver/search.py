from collections import deque
from app.cube.state import CubeState
from app.cube.moves import apply_move

class BreadthFirstSearch:

    def __init__(self):
        # All 18 standard moves
        self.moves = [
            "U", "U'", "U2",
            "D", "D'", "D2",
            "R", "R'", "R2",
            "L", "L'", "L2",
            "F", "F'", "F2",
            "B", "B'", "B2",
        ]

    @staticmethod
    def state_key(state: CubeState):
        """creating a hashable key for a cube state"""
        return (tuple(state.cp), tuple(state.co))

    @staticmethod
    def reconstruct_path(parent, current_key):
        """Reconstruct the solution by following parent records."""
        path = []

        while parent[current_key] is not None:
            previous_key, move = parent[current_key]
            path.append(move)
            current_key = previous_key

        path.reverse()
        return path

    def breadth_first_search(self, start_state: CubeState):
        """
        Find a shortest solution using BFS.

        Returns a list of moves if a solution is found,
        or None if no solution is found.
        """

        if not start_state.is_valid():
            raise ValueError("The start state of the cube is invalid")

        if start_state.is_solved():
            return []

        start_key = self.state_key(start_state)

        queue = deque([start_state])
        visited = {start_key}

        # Maps each discovered state to (previous state key, move).
        # The initial state has no parent.
        parent = {
            start_key : None
        }

        while queue:
            current_state = queue.popleft()
            current_key = self.state_key(current_state)

            for move in self.moves:
                next_state = apply_move(current_state, move)
                next_key = self.state_key(next_state)

                if next_key in visited:
                    continue

                visited.add(next_key)
                parent[next_key] = (current_key, move)

                if next_state.is_solved():
                    return self.reconstruct_path(parent, next_key)

                queue.append(next_state)

        return None
    

    

    

    




























# def breadth_first_search(start: CubeState, max_depth: int = 8) -> list[str] | None:
#     """Find a shortest solution for small scrambles."""
#     # TODO: use a deque of (state, path), a visited set, all legal moves, and
#     # stop expanding paths at max_depth. This is the first algorithm to learn.
#     raise NotImplementedError


# def depth_limited_search(start: CubeState, limit: int) -> list[str] | None:
#     """Explore one depth limit using recursive depth-first search."""
#     # TODO: implement recursive backtracking and avoid immediate reversals.
#     raise NotImplementedError


# def iterative_deepening_search(start: CubeState, max_depth: int) -> list[str] | None:
#     """Repeat depth-limited search with limits 0..max_depth."""
#     # TODO: call depth_limited_search for each limit and return first solution.
#     raise NotImplementedError


# def ida_star(start: CubeState, max_depth: int = 14) -> list[str] | None:
#     """Final intended search: iterative deepening plus a heuristic bound."""
#     # TODO: implement thresholded DFS using f = g + h and lower_bound(state).
#     raise NotImplementedError

