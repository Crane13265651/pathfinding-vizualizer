import pygame

WHITE = (255, 255, 255)
GREY = (200, 200, 200)

class Node:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size

        self.x = row * size
        self.y = col * size

        self.color = WHITE
        self.is_wall = False  

    def draw(self, window):
        pygame.draw.rect(
            window,
            self.color,
            (self.x, self.y, self.size, self.size)
        )

    def make_wall(self):
        self.is_wall = True
        self.color = (0, 0, 0)  

    def reset(self):
        self.is_wall = False
        self.color = (255, 255, 255)  