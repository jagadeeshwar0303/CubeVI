from dataclasses import dataclass

FACES = ("U", "F", "R", "B", "L", "D")
COLOURS = ("W", "B", "O", "G", "R", "Y")
FACE_SIZE = 4
STICKER_COUNT = len(FACES) * FACE_SIZE
ALLOWED_COLOURS = frozenset(COLOURS)


SOLVED_FACE_COLOURS = dict(zip(FACES, COLOURS))


@dataclass(frozen=True)
class CubeState:
    """Immutable 24-sticker state: U, F, R, B, L, D, four stickers each."""
    stickers: tuple[str, ...]

    def __post_init__(self):
        stickers = tuple(sticker.strip().upper() for sticker in self.stickers)

        if len(stickers) != STICKER_COUNT:
            raise ValueError("A 2x2x2 cube must contain exactly 24 stickers")

        if set(stickers) - ALLOWED_COLOURS:
            raise ValueError("Use only W, B, O, G, R, Y as sticker colours")

        if any(stickers.count(colour) != FACE_SIZE for colour in COLOURS):
            raise ValueError("Each colour must appear exactly four times")

        object.__setattr__(self, "stickers", stickers)

    @classmethod
    def solved(cls):
        solved_stickers = tuple(
            SOLVED_FACE_COLOURS[face]
            for face in FACES
            for _ in range(FACE_SIZE)
        )
        return cls(solved_stickers)

    @classmethod
    def from_faces(cls, faces: dict[str, list[str]]):
        if set(faces) != set(FACES):
            raise ValueError("Exactly U, F, R, B, L, D faces are required")

        if any(len(faces[face]) != FACE_SIZE for face in FACES):
            raise ValueError("Each face must contain four stickers")

        stickers = tuple(value for face in FACES for value in faces[face])
        return cls(stickers)

    def to_faces(self):
        return {
            face: list(self.stickers[index * FACE_SIZE:index * FACE_SIZE + FACE_SIZE])
            for index, face in enumerate(FACES)
        }

    def is_solved(self):
        return all(
            len(set(self.stickers[index:index + FACE_SIZE])) == 1
            for index in range(0, STICKER_COUNT, FACE_SIZE)
        )