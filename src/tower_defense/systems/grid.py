#grid takes in a width and height of the screen
# is just vertical and horizontal lines that are drawn on the screen
# x increases by tile size until it reaches the width of the screen
# y increases by tile size until it reaches the height of the screen
# tile size is calculated based  on w = 800 h = 600
# 20 columns and 15 rows
import pygame

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_size = 40
        self.row_count = height // self.tile_size
        self.col_count = width // self.tile_size
        self.color = (255, 255, 255)

# how can i use pygame.draw lines to draw the grid on the screen and pygame draw rect to draw the grid on the screen
    def draw(self, screen):
        #draw the rows
        for row in range(self.row_count+1):
            y = min(row * self.tile_size, self.height - 1)
            pygame.draw.line(screen, self.color, (0, y), (self.width-1, y))
        for col in range(self.col_count+1):
            x = min(col * self.tile_size, self.width - 1)
            pygame.draw.line(screen, self.color, (x, 0), (x, self.height-1))
            EMPTY = -1
    def get_tile(self, row, col):
        if row < 0 or row >= self.row_count or col < 0 or col >= self.col_count:
            return None
        return (row, col)
    def draw_map(self, screen, map_data):
        tiles = map_data.get_map()

        for row in range(self.row_count):
            for col in range(self.col_count):
                tile = tiles[row][col]
                if tile != -1:
                    x = col * self.tile_size
                    y = row * self.tile_size
                    pygame.draw.rect(screen, (255, 0, 0), (x, y, self.tile_size, self.tile_size))