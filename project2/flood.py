from utilities import *
from cheating import ADJACENCY_LIST
# adjacency list

def flood(color_of_tile, flooded_list, screen_size):
    region_color = color_of_tile[flooded_list[0]]
    print 'region_color %s' % region_color

    #return
    flooded_set = set(flooded_list)
    visited_tiles = set()

    def follow_adjacent(coords):
        if coords in visited_tiles or color_of_tile[coords] != region_color:
            visited_tiles.add(coords) # adds to visited if not there already
            return
        else:
            # this tile is now flooded and visited
            flooded_set.add(coords)
            visited_tiles.add(coords)

            # mutate the flooded_list as well
            flooded_list.append(coords)

            neighbors = ADJACENCY_LIST[coords]
            # neighbors are all edges

            for neighbor in neighbors:
                # recur on the neighbors
                follow_adjacent(neighbor)


    for tile in flooded_list:
        follow_adjacent(tile)
