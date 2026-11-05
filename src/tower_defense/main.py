import pygame
from tower_defense.systems.grid import Grid
from tower_defense.systems.map_data import MapData
fps = 60
def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    running = True
    grid = Grid(screen.get_width(), screen.get_height())
    map_data = MapData(grid.row_count, grid.col_count)
    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN: 
                tile = grid.get_tile(event.pos[1] // grid.tile_size, event.pos[0] // grid.tile_size)       
                if tile is not None:
                    row, col = tile
                    map_data.set_tile(row, col, 1)
        #fill screen with black
        screen.fill((0, 0, 0))
        #draw the grid
        grid.draw_map(screen, map_data)
        pygame.display.flip()
        #limit to 60 fps
        dt = clock.tick(fps) / 1000.0
    pygame.quit()


if __name__ == "__main__":
    main()