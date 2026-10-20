FACES = ("U", "F", "R", "B", "L", "D")
COLOURS = ("W", "B", "O", "G", "R", "Y")

class CubeState:
    def __init__(self, stickers):
        cleaned_stickers = []

        for sticker in stickers:
            cleaned_sticker = sticker.strip().upper()
            cleaned_stickers.append(cleaned_sticker) #removing the spaces and converting to uppercase for uniformity

        if len(cleaned_stickers) != 24:
            raise ValueError("A cube must contain exactly 24 stickers") #a string must be of length 24 to represent a cube, not less not more.

        for sticker in cleaned_stickers:
            if sticker not in COLOURS:
                raise ValueError("Use only W, B, O, G, R, Y as sticker colours") #verifiying if the stickers are only from the allowed colours i.e are they valid or not.

        for colour in COLOURS:
            if cleaned_stickers.count(colour) != 4:
                raise ValueError("Each colour must appear exactly four times") #a particular color  must appear exactly 4 times on a cube, if not then it is an invalid cube.

        # Finally a tuple of immutable stickers stored in the instance variable for comparison and hashing purposes.
        self.stickers = tuple(cleaned_stickers)

    def __eq__(self,other):
        if not isinstance(other, CubeState):
            return False

        return self.stickers == other.stickers



    def solved(self):
        stickers=[]
        for color in COLOURS:
            for i in range(4):
                stickers.append(color)

        return CubeState(stickers)

    def is_solved(self):
        pivot = 0

        # cube is solved when all the four stickers of each face match

        for face in FACES:
           for number in range(4):
                current_sticker = self.stickers[pivot + number]

                if current_sticker != self.stickers[pivot]:  #self.sticker[pivot] is the first sticker of that particular face.
                    return False
           pivot += 4

        return True

    def from_faces(faces):
        # confirming all the faces are present
        if not all(x in faces for x in FACES):
            raise ValueError("Missing one or more faces. All six faces must be present.")

        # rejecting additional face names too.
        if len(faces) != 6:
            raise ValueError("Too many faces. Only six faces are allowed.")

        stickers = []

        #reading each face in the same fixed FACES order.
        for i in FACES:
            face_stickers = faces[i]

            if len(face_stickers) != 4:
                raise ValueError(f"Face {i} must have exactly four stickers.")

            for j in face_stickers:
                stickers.append(j)

        return CubeState(stickers)

    def to_faces(self):
        faces_dict = {}
        pivot = 0

        # Take four stickers at a time and assign them to a face.
        for i in FACES:
            faces_dict[i] = []

            for number in range(4):
                faces_dict[i].append(self.stickers[pivot]) #self.stickers[pivot] is the first sticker of that particular face.
                pivot += 1

        return faces_dict
    #at the end the to_faces dictionary looks like this:
    # """
    # {
    #     "U": ["W", "W", "W", "W"],
    #     "F": ["B", "B", "B", "B"],
    #     "R": ["O", "O", "O", "O"],
    #     "B": ["G", "G", "G", "G"],
    #     "L": ["R", "R", "R", "R"],
    #     "D": ["Y", "Y", "Y", "Y"]
    # }"""



