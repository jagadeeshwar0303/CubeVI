from fastapi import APIRouter, HTTPException
from app.cube.scramble import generate_scramble
from app.cube.state import CubeState
from app.nlp.parser import parse_constraint
from app.schemas import SolveRequest, SolveResponse
from app.solver.solver import solve

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/scramble")
def scramble(length: int = 6):
    moves, cube = generate_scramble(length)
    return {"scramble": moves, "faces": cube.to_faces()}

@router.post("/solve", response_model=SolveResponse)
def solve_cube(request: SolveRequest):
    try:
        cube = CubeState.from_faces(request.faces)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    parsed = parse_constraint(request.constraint)
    result = solve(cube, parsed)
    if result is None:
        raise HTTPException(status_code=422, detail="No solution found within the search depth")
    return SolveResponse(valid=True, moves=result.moves, depth=len(result.moves), explanation=result.explanation, parsed_constraint=parsed)

