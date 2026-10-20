class CubeState:
    """
    Represents the state of a 2x2x2 Rubik's Cube.

    Corner position IDs:
        0 = URF
        1 = UFL
        2 = ULB
        3 = UBR
        4 = DFR
        5 = DLF
        6 = DBL
        7 = DRB

    cp[i] = corner piece occupying position i
    co[i] = orientation of the corner at position i
    """
    CORNER_NAMES = (
            'URF', 'UFL', 'ULB', 'UBR',
            'DFR', 'DLF', 'DBL', 'DRB'
    )


    def __init__(self, cp=None, co=None):

        # corner permutation : self.co is the singel purnutation of 8 corners (0 - 7) 
        self.cp = (
            cp.copy() if cp is not None
            else list(range(8))
        )

        # corner orientations : each corner will have it's own orientations (0 or 1 or 2)
        self.co = (
            co.copy() if co is not None
            else [0] * 8
        )

    def is_solved(self):
        """returns True if the cube is solved else False"""

        return (
            self.cp == list(range(8))
            and self.co == [0] * 8
        )

    def is_valid(self):
        """ valid cube state : state which is achievable from the solved state using valid moves
        returns True if the cube state is valid otherwise False """

        return (
            len(self.cp) == 8
            and len(self.co) == 8
            and sorted(self.cp) == list(range(8))
            and all(o in [0, 1, 2] for o in self.co)
            and sum(self.co) % 3 == 0
        )


    def __repr__(self):
        return f"CubeState(cp={self.cp}, co={self.co})"