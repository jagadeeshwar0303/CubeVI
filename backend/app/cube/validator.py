from app.cube.state import CubeState

def validate_cube(faces):
    try:
        CubeState.from_faces(faces)
    except ValueError as error:
        return False, str(error)
    return True, "Cube input is structurally valid."

