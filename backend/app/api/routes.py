"""HTTP routes: web requests translated into application-service calls."""

from fastapi import APIRouter, HTTPException

from app.schemas import ScrambleResponse, SolveRequest, SolveResponse

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    """Health check used by the frontend and deployment tooling."""
    return {"status": "ok"}


@router.get("/scramble", response_model=ScrambleResponse)
def scramble(length: int = 6) -> ScrambleResponse:
    """Return a demo scramble and its resulting face colours."""
    # TODO: validate length, call generate_scramble(), and serialize the state.
    raise HTTPException(status_code=501, detail="Scramble route is a learning TODO")


@router.post("/solve", response_model=SolveResponse)
def solve_cube(request: SolveRequest) -> SolveResponse:
    """Validate, parse, solve, and serialize one user request."""
    # TODO: construct CubeState, parse request.constraint, call solve(), then map
    # invalid input to 400 and no-solution results to 422.
    raise HTTPException(status_code=501, detail="Solve route is a learning TODO")

