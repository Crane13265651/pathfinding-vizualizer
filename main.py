import pygame
from node import Node

WIDTH = 800
ROWS = 50
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualizer")


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap)
            grid[i].append(node)
    return grid


def draw(window, grid):
    window.fill((0, 0, 0))
    for row in grid:
        for node in row:
            node.draw(window)
            pygame.draw.rect(window, (200, 200, 200), (node.x, node.y, node.size, node.size), 1)
    pygame.display.update()

grid = make_grid(ROWS, WIDTH)

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

running = True
while running:
    draw(WINDOW, grid)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]: 
            pos = pygame.mouse.get_pos()
            row, col = get_clicked_pos(pos, ROWS, WIDTH)
            node = grid[row][col]
            node.make_wall()

        elif pygame.mouse.get_pressed()[2]:  
            pos = pygame.mouse.get_pos()
            row, col = get_clicked_pos(pos, ROWS, WIDTH)
            node = grid[row][col]
            node.reset()

pygame.quit()