import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
#Define colors for different types of nodes
EMPTY = (255, 255, 255) # this is white
VISIT = (128, 0, 128) # this is purple
OBS = (0, 0, 0) # this is black
END = (0,0, 255) # fix this color later
BEGIN = (255, 0, 0) #this is red color
PATH =  (200, 100, 40)
pygame.display.set_caption("A* Path Finding Algorithm")


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self. width = width
        self.total_rows = total_rows
        self.x = row * width
        self.y = col * width
        self.neighbors = [] 
        self.color = EMPTY
        
    def mark_start(self):
        self.color = BEGIN
    
    def mark_end(self):
        self.color = END 

    def mark_block(self):
        self.color = OBS

    def is_visited(self):
        return self.color == VISIT
    
    def is_empty(self):
        return self.color == EMPTY
    
    def is_block(self):
        return self.color == OBS

    def is_start(self):
        return self.color == BEGIN
    
    def is_end(self):
        return self.color == END 
    
    def reset(self):
        self.color = EMPTY
    #this is for figuring out mouse click position
    def pos(self):
        return self.row, self.col

    def make_path(self):
        self.color = PATH

   #this is drawing cubes on grib with colors 
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    
    def update_neighbors(self, grid):
        self.neighbors = []
        #add upper node
        if self.row > 0 and not grid[self.row -1][self.col].isblock():
            self.neighbors.append(grid[self.row - 1][self.col])

        #add lower node
        if self.row < len(grid) - 1 and not grid[self.row + 1][self.col].is_block():
            self.neighbors.append(grid[self.row + 1][self.col])

        #add right node
        if self.col < len(grid[0]) -1 and not grid[self.row][self.col + 1].is_block():
            self.neighbors.append(grid[self.row][self.col + 1])

        #add left node
        if self.col > 0 and not grid[self.row][self.col - 1].is_block():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False

#making 2-D list for all nodes on the grid
def make_grid(rows, width):
    length = width // rows
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, length, rows)
            grid[i].append(node)

    return grid

def draw_grid(win, rows, width):
    length = width // rows
    for i in range(rows):
        pygame.draw.line(win, OBS, (0, i * length), (width, i * length))
        for j in range(rows):
            pygame.draw.line(win, OBS, (j * length, 0), (j * length, width))

def draw_all(win, grid, rows, width):
    #initialize the canvas to full white before drawing anything else
    win.fill(EMPTY)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()

#the x, y concept is little confusing, x mean col and y mean row, thus we need to swtich them
def get_pos(pos, rows, width):
    x, y = pos
    length = width // rows
    row, col = x // length, y // length
    return row, col


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)
    start = None
    end = None
    running = True
    while running:
        draw_all(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #check when mouse is clicked. We have to change the node color
            if pygame.mouse.get_pressed()[0]: #this is left click
                pos = pygame.mouse.get_pos() 
                row, col = get_pos(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    node.mark_start()
                elif not end and node != start:
                    end = node
                    node.mark_end()
                elif node != start and node != end:
                    node.mark_block()
            elif pygame.mouse.get_pressed()[2]: # this is right click
                pos = pygame.mouse.get_pos()
                row, col = get_pos(pos, ROWS, width)
                node = grid[row][col]
                if node == start:
                    start = None
                    node.reset()
                elif node == end:
                    end = None
                    node.reset()
                else:
                    node.reset()



    pygame.quit()

main(WIN, WIDTH)
