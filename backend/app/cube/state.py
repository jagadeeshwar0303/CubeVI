FACES = ("U", "F", "R", "B", "L", "D")
COLOURS = ("W", "B", "O", "G", "R", "Y")

class CubeState:
    def __init__(self, stickers):
        cleaned_stickers = []

        # Make every sticker uppercase and remove accidental spaces.
        for sticker in stickers:
            cleaned_sticker = sticker.strip().upper()
            cleaned_stickers.append(cleaned_sticker)

        # A 2x2 cube has 6 faces, with 4 stickers on each face.
        if len(cleaned_stickers) != 24:
            raise ValueError("A cube must contain exactly 24 stickers")

        # Check that every sticker uses one of the allowed colours.
        for sticker in cleaned_stickers:
            if sticker not in COLOURS:
                raise ValueError("Use only W, B, O, G, R, Y as sticker colours")

        # Each colour must occur exactly four times.
        for colour in COLOURS:
            colour_count = cleaned_stickers.count(colour)

            if colour_count != 4:
                raise ValueError("Each colour must appear exactly four times")

        # A tuple prevents the stickers from being changed by accident later.
        self.stickers = tuple(cleaned_stickers)

    def __eq__(self, other):
        if not isinstance(other, CubeState):
            return False

        return self.stickers == other.stickers

    def solved():
        stickers = []

        # FACES and COLOURS have matching positions:
        # U -> W, F -> B, R -> O, B -> G, L -> R, D -> Y
        for colour in COLOURS:
            for number in range(4):
                stickers.append(colour)

        return CubeState(stickers)