"""Search algorithms for the AI portion of CubeVI."""

from app.cube.state import CubeState


def breadth_first_search(start: CubeState, max_depth: int = 8) -> list[str] | None:
    """Find a shortest solution for small scrambles."""
    # TODO: use a deque of (state, path), a visited set, all legal moves, and
    # stop expanding paths at max_depth. This is the first algorithm to learn.
    raise NotImplementedError


def depth_limited_search(start: CubeState, limit: int) -> list[str] | None:
    """Explore one depth limit using recursive depth-first search."""
    # TODO: implement recursive backtracking and avoid immediate reversals.
    raise NotImplementedError


def iterative_deepening_search(start: CubeState, max_depth: int) -> list[str] | None:
    """Repeat depth-limited search with limits 0..max_depth."""
    # TODO: call depth_limited_search for each limit and return first solution.
    raise NotImplementedError


def ida_star(start: CubeState, max_depth: int = 14) -> list[str] | None:
    """Final intended search: iterative deepening plus a heuristic bound."""
    # TODO: implement thresholded DFS using f = g + h and lower_bound(state).
    raise NotImplementedError

