from utilities import up, right, down, left, in_bounds, STEP_SIZE
from itertools import chain

# Size code uplicates screen_size code from floodit.py
# but I recreate the size here so that I don't have to
# alter floodit.py
board_size = 14
def get_screen_size(bsize):
    return (max(bsize * STEP_SIZE + 160, 608), max(bsize * STEP_SIZE, 448))

SCREEN_SIZE = get_screen_size(board_size)

def neighbors(central_coord):
    neighbor_creators = tuple((up, right, down, left))
    neighbors = []
    for neighbor_func in neighbor_creators:
        potential_neighbor = neighbor_func(central_coord)
        if in_bounds(potential_neighbor, SCREEN_SIZE):
            neighbors.append(potential_neighbor)
    return neighbors


def adjacency_list(screen_size, step):
    screen_x_limit, screen_y_limit = screen_size[0], screen_size[1]
    tiles = [[(x, y) for y in xrange(0, screen_y_limit, step)] for x in xrange(0, screen_x_limit, step)]
    
    edge_list = {coord: None for coord in chain.from_iterable(tiles)}

    for vertex in edge_list.keys():
        edge_list[vertex] = neighbors(vertex)

    return edge_list

#ADJACENCY_LIST = adjacency_list(SCREEN_SIZE, STEP_SIZE)

def _main():
    matrix = adjacency_list(SCREEN_SIZE, STEP_SIZE)
    print SCREEN_SIZE
    for vertex in matrix:
        #print "%s : %s" % (vertex, matrix[vertex])
        pass

if __name__ == '__main__':
    _main()
