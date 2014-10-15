
class ParentDirection:
    UP = "UP"
    LEFT = "LEFT"
    DIAG = "DIAG"

SPACE_CHAR = '_'

class AlignmentCell(object):
    def __init__(self, i, j, xstring, ystring, scoringFunc, board, parentDirection=None):
        self.i, self.j = i, j
        self.xtring, self.ystring = xstring, ystring
        self.board = board
        self.scoringFunc = scoringFunc
        self.parent = parent

    """
    @property
    def parent(self):
        if parentDirection == None:
            return None
        elif parentDirection == ParentDirection.UP:
            return self.board[self.j-1][self.i]
        elif parentDirection == ParentDirection.LEFT:
            return self.board[self.j][self.i-1]
        elif parentDirection == ParentDirection.DIAG:
            return self.board[self.j-1][self.i-1]
        else:
            raise TypeError('parentDirection need be a ParentDirection enum value')
        

    @property
    def parentRelation(self):
        if self.i == 0 and self.j == 0:
            return None

        up = self.board[self.j-1][self.i] if j
        left = self.board[self.j][self.i-1]
        diag = self.board[self.j-1][self.i-1]

        elif self.parent.i == self.i - 1 and self.parent.j == self.j - 1:
            return ParentDirection.DIAG
        elif self.parent.i == self.i - 1 and self.parent.j == self.j:
            return ParentDirection.LEFT
        elif self.parent.i == self.i and self.parent.j == self.j - 1:
            return ParentDirection.UP
        else:
            raise ValueError('the parent cannot be where it is')
            
        
    
    @property
    def value(self):       
        x, y = self.i - 1, self.j - 1

        if not self.parent:
            return 0

        if self.parentRelation == ParentDirection.UP:
            return self.parent.value + self.scoringFunc(SPACE_CHAR, self.ystring[y])
        elif self.parentRelation == ParentDirection.LEFT:
            return self.parent.value + self.scoringFunc(self.xstring[x], SPACE_CHAR)
        else:
            return self.parent.value + self.scoringFunc(self.xtring[x], self.ystring[y])

    @property
    def choice(self):
        if not self.parent:
            return None

        relations = {ParentDirection.UP: 'I',
                     ParentDirection.LEFT: 'D',
                     ParentDirection.DIAG: 'M'}
        return relations[self.parent]


    def __repr__(self):
        return "<ACell %s, %s>" % (self.i, self.j)
    """
