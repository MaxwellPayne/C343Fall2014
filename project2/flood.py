from utilities import *
from adjacency import adjacency_list, get_screen_size
# bring in the adjacency list from the cheat

_ADJACENCY_LIST = None

def flood(color_of_tile, flooded_list, screen_size):
    global _ADJACENCY_LIST
    if not _ADJACENCY_LIST:
        from math import sqrt
        board_size = sqrt(len(color_of_tile))
        actual_screen_size = get_screen_size(board_size)
        _ADJACENCY_LIST = adjacency_list(actual_screen_size, STEP_SIZE)

    region_color = color_of_tile[flooded_list[0]]
    # the region color will be color of origin

    flooded_set = set(flooded_list)
    # set of all flooded tiles; allows constant-time lookup
    visited_tiles = set()
    # set of all tiles visited this round

    def follow_adjacent(coords):
        """Tests to see if coords is same color as region,
        if so adds it to the flooded list and recurs on
        the neighboring tiles"""
        if coords in visited_tiles or color_of_tile[coords] != region_color:
            visited_tiles.add(coords) # adds to visited if not there already
            return
        else:
            # this tile is now flooded and visited
            flooded_set.add(coords)
            visited_tiles.add(coords)

            # mutate the flooded_list as well
            flooded_list.append(coords)

            # neighbors are all the coords' edges
            neighbors = _ADJACENCY_LIST[coords]

            for neighbor in neighbors:
                # recur on the neighbors
                follow_adjacent(neighbor)

    for tile in flooded_list:
        follow_adjacent(tile)
