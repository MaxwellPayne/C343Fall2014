#! /usr/bin/env python

import sys, time, random
import pygame

e_aplh = "abcdefghijklmnopqrstuvwxyz"
dna_alph = "ACGT"

# generate random string drawn from the given alphabet and of a given length
def gen_random_string(alphabet, length):
    a_len = len(alphabet)
    ret = ""
    for n in range(length):
        ret += alphabet[random.randint(0, a_len-1)]
    return ret

# print gen_random_string(e_aplh, 5)

SPACE_CHAR = '_'
SPACE_PENALTY = -1

# the scoring function
def s(x, y):
    if x == SPACE_CHAR or y == SPACE_CHAR:
        return SPACE_PENALTY
    elif x == y:
        return 2
    else:
        return -2

TILE_SIZE = 40
tile_color = (255, 255, 255)
highlight_color = (120, 129, 250)

def init_board(m, n):
    screen = pygame.display.set_mode(((m+2)*TILE_SIZE, (n+2)*TILE_SIZE))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Dot Board')
    pygame.font.init()
    font = pygame.font.Font(None, 15)
    return screen, font

def create_tile(font, text, color):
    tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
    tile.fill(color)
    b1 = font.render(text, 1, (0, 0, 0))
    tile.blit(b1, (TILE_SIZE/2, TILE_SIZE/2))
    return tile

def render_board(board, font, s1, s2, F):
    for i in range(len(s1)):
        tile = create_tile(font, s1[i], tile_color)
        board.blit(tile, ((i+2)*TILE_SIZE, 0))
    tile = create_tile(font, '', tile_color); board.blit(tile, (0, 0))
    tile = create_tile(font, '', tile_color); board.blit(tile, (TILE_SIZE, 0))
    for j in range(len(s2)):
        tile = create_tile(font, s2[j], tile_color)
        board.blit(tile, (0, (j+2)*TILE_SIZE))
    tile = create_tile(font, '', tile_color); board.blit(tile, (0, TILE_SIZE))
    for (x,y) in sorted(F.keys()):
        tile = create_tile(font, str(F[(x,y)]), tile_color)
        board.blit(tile, ((x+1)*TILE_SIZE, (y+1)*TILE_SIZE))

class ParentDirection:
    """Enum of direction relationships"""
    UP = "I"
    LEFT = "D"
    DIAG = "M"

class Cell:
    """A cell in a dynamic programming matrix that has a
    value and remembers where its parent came from"""
    def __init__(self, val, direction):
        self.val, self.direction = val, direction

    def __repr__(self):
        return '<Cell %s %s>' % (self.val, self.direction)

    def __cmp__(self, other):
        """Allows Cells to be compared greater/less than by their val"""
        return cmp(self.val, other.val)


def seq_align(s1, s2, enable_graphics=True):
    strX, strY = s1, s2
    matrix = [[None for _ in range(len(strX) + 1)] for _ in range(len(strY) + 1)]

    for r, row in enumerate(matrix):
        for c, col in enumerate(matrix):
            if r == 0 and c == 0: # top left corner
                matrix[r][c] = Cell(0, None)
            elif r == 0: # look left
                matrix[r][c] = Cell(-c, ParentDirection.LEFT)
            elif c == 0: # look up
                matrix[r][c] = Cell(-r, ParentDirection.UP)
            else: # evaluate to look up, left, or diag
                up, left, diag = matrix[r-1][c], matrix[r][c-1], matrix[r-1][c-1]
                # x and y indices for the strings
                x, y = c-1, r-1
                
                # each 'using' is a possible new cell for this space, using different parents
                usingUp = Cell(up.val + s(strX[x], SPACE_CHAR), ParentDirection.UP)
                usingLeft = Cell(left.val + s(SPACE_CHAR, strY[y]), ParentDirection.LEFT)
                usingDiag = Cell(diag.val + s(strX[x], strY[y]), ParentDirection.DIAG)
                # optimal choice is the cell with the maximum value
                optimal = max((usingUp, usingLeft, usingDiag))
                matrix[r][c] = optimal
                
    for r in matrix:
        print r

# commented out for now so we can more specifically test
# the seq_align function    
"""
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    f=open('tests.txt', 'r');tests= eval(f.read());f.close()
    cnt = 0; passed = True
    for ((s1, s2), (a1, a2)) in tests:
        (ret_a1, ret_a2) = seq_align(s1, s2, False)
        if (ret_a1 != a1) or (ret_a2 != a2):
            print("test#" + str(cnt) + " failed...")
            passed = False
        cnt += 1
    if passed: print("All tests passed!")
elif len(sys.argv) == 2 and sys.argv[1] == 'gentests':
    tests = []
    for n in range(25):
        m = random.randint(8, 70); n = random.randint(8, 70)
        (s1, s2) = (gen_random_string(dna_alph, m), gen_random_string(dna_alph, n))
        (a1, a2) = seq_align(s1, s2, False)
        tests.append(((s1, s2), (a1, a2)))
    f=open('tests.txt', 'w');f.write(str(tests));f.close()
else:
    l = [('ACACACTA', 'AGCACACA'), ('IMISSMISSISSIPI', 'MYMISSISAHIPPIE')]
    enable_graphics = True
    if enable_graphics: pygame.init()
    for (s1, s2) in l:
        print 'sequences:'
        print (s1, s2)
        
        m = len(s1)
        n = len(s2)
        
        print 'alignment: '
        print seq_align(s1, s2, enable_graphics)
    
    if enable_graphics: pygame.quit()
"""

if __name__ == '__main__':
    seq_align("ACACACTA", "AGCACACA")
