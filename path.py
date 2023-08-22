import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
#Define colors for different types of nodes
EMPTY = (255, 255, 255) # this is white
VISIT = (128, 0, 128) # this is purple
OBS = (0, 0, 0) # this is black
END = (200, 230,100) # fix this color later
BEGIN = (13, 44, 20) #i don't know what color it is, fix it later
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
    #this is for figuring out mous click position
    def pos(self):
        return self.row, self.col

    def make_path(self):
        self.color = PATH

   #this is drawing cubes on grib with colors 
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    
    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False

#making 2-D list for all nodes on the grid
def make_grid(rows, width):
    length = width // rows
    grid = []
    for i in rows:
        add = []
        for j in rows:
            node = Node(i, j, length, rows)

def draw_grid(win, rows, width):
    length = width // rows
    for row in rows:
        for col in rows:


def draw_all(win, grid, rows, width):
    pass

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)
    start = None
    end = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #check when mouse is clicked. We have to change the node color


    pygame.quit()

main(WIN, WIDTH)