import pygame
import random

import map
import pathfinding


TILE_SIZE = 25
MAP_WIDTH = 20
MAP_HEIGHT = 20


def draw_map_and_path(screen, the_map, path=None):
    if type(the_map) == list:
        the_map = map.Map((MAP_WIDTH, MAP_HEIGHT), the_map, TILE_SIZE, include_diagonals=True)

    if path is None:
        path = get_path(the_map)

    screen.fill((255, 255, 255))

    the_map.draw(screen)
    for i in range(1, len(path)):
        pygame.draw.line(screen, (0, 0, 0), path[i - 1].pos, path[i].pos, 6)

    pygame.display.flip()


def get_path(the_map):
    path = pathfinding.a_star_search(the_map, None)
    if path is None:
        path = []

    #pathfinding.pull_string(the_map, path)

    return path


def calculate_fitness(the_map):
    if type(the_map) == list:
        the_map = map.Map((MAP_WIDTH, MAP_HEIGHT), the_map, TILE_SIZE, include_diagonals=True)
    path = get_path(the_map)
    return pathfinding.get_path_length(path)


def main():
    # Initialise PyGame
    pygame.init()
    clock = pygame.time.Clock()

    window_width = MAP_WIDTH * TILE_SIZE
    window_height = MAP_HEIGHT * TILE_SIZE
    window_size = (window_width, window_height)

    # Create the screen
    screen = pygame.display.set_mode(window_size)

    # Initial map
    tiles = [' '] * (MAP_WIDTH * MAP_HEIGHT)
    tiles[0] = 'S'
    tiles[-1] = 'G'

    fitness = calculate_fitness(tiles)

    print("Current fitness:", fitness)
    draw_map_and_path(screen, tiles)

    while True:
        new_tiles = tiles[:]
        tile_index = random.randrange(len(new_tiles))
        if new_tiles[tile_index] == ' ':
            new_tiles[tile_index] = '*'
        elif new_tiles[tile_index] == '*':
            new_tiles[tile_index] = ' '
        new_fitness = calculate_fitness(new_tiles)

        if False:
            tiles = new_tiles
            fitness = new_fitness

            print("Current fitness:", fitness)
            draw_map_and_path(screen, tiles)

        pygame.event.get()

if __name__ == '__main__':
    main()
