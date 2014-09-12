import sys
from utilities import *

sys.setrecursionlimit(2000)

def neighbors(central_coord, screen_size):
    neighbor_creators = tuple((up, right, down, left))
    neighbors = []
    for neighbor_func in neighbor_creators:
        potential_neighbor = neighbor_func(central_coord)
        if in_bounds(potential_neighbor, screen_size):
            neighbors.append(potential_neighbor)
    return neighbors

def flood(color_of_tile, flooded_list, screen_size):
    visited_tiles=[]
    region_color=color_of_tile[flooded_list[0]]

    def follow_adjacent(coords):
        """Tests to see if coords is same color as region,
        if so adds it to the flooded list and recurs on
        the neighboring tiles"""
        if coords in visited_tiles:
            return
        elif color_of_tile[coords] != region_color:
        	visited_tiles.append(coords) # adds to visited if not there already
        	return
        else:
            # this tile is now flooded and visited
            visited_tiles.append(coords)

            # mutate the flooded_list as well
            flooded_list.append(coords)

            # neighbors are all the coords' edges
            neighbors = neighbors(coords, screen_size)

            for neighbor in neighbors:
                # recur on the neighbors
                follow(neighbor)

    for tile in flooded_list:
      	follow(tile)


