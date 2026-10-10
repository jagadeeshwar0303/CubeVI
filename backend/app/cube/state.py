from dataclasses import dataclass

FACES = ("U", "R", "F", "D", "L", "B")
COLOURS = frozenset({"W", "R", "G", "Y", "O", "B"})

@dataclass(frozen=True)
class CubeState:
    """Immutable 24-sticker state: U, R, F, D, L, B, four stickers each."""
    stickers: tuple[str, ...]

    @classmethod
    def solved(cls):
        return cls(tuple(face for face in FACES for _ in range(4)))

    @classmethod
    def from_faces(cls, faces: dict[str, list[str]]):
        if set(faces) != set(FACES):
            raise ValueError("Exactly U, R, F, D, L, B faces are required")
        if any(len(faces[face]) != 4 for face in FACES):
            raise ValueError("Each face must contain four stickers")
        stickers = tuple(value.upper() for face in FACES for value in faces[face])
        if set(stickers) - COLOURS or any(stickers.count(c) != 4 for c in COLOURS):
            raise ValueError("Use W, R, G, Y, O, B, with each colour appearing four times")
        return cls(stickers)

    def to_faces(self):
        return {face: list(self.stickers[i * 4:i * 4 + 4]) for i, face in enumerate(FACES)}

    def is_solved(self):
        return all(len(set(self.stickers[i:i + 4])) == 1 for i in range(0, 24, 4))

