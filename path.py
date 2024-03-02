import pygame
import math
from queue import PriorityQueue



WIDTH = 800
ROWS = 40
WIN = pygame.display.set_mode((WIDTH, WIDTH))
ALG = "a_star"
# Define colors for different types of nodes
EMPTY = (255, 255, 255)  # this is white
VISIT = (174, 214, 220) #lightblue node that is already visited
OBS = (0, 0, 0)  # this is black
END = (5, 13, 255)  # this is blue color for now
BEGIN = (255, 0, 0)  # this is red color
FINAL = (244,137,139) #pink, this is a node that is being considered as one of current node's neighbor
PATH = (0,21,79) #dark navy
MODE = "RUN"
pygame.display.set_caption("PathFinding Algorithm")


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x = row * width
        self.y = col * width
        self.neighbors = []
        self.color = EMPTY
        self.g = float('inf')
        self.f = float('inf')

    def mark_start(self):
        self.color = BEGIN

    def mark_end(self):
        self.color = END

    def mark_block(self):
        self.color = OBS

    def mark_closed(self):
        self.color = VISIT

    def mark_open(self):
        self.color = PATH

    def mark_path(self):
        self.color = FINAL

    def is_closed(self):
        return self.color == VISIT

    def is_open(self):
        return self.color == EMPTY

    def is_block(self):
        return self.color == OBS

    def is_start(self):
        return self.color == BEGIN

    def is_end(self):
        return self.color == END

    def reset(self):
        self.color = EMPTY
        self.f = float('inf')
        self.g = float('inf')

    # this is for figuring out mouse click position
    def pos(self):
        return self.row, self.col

    def make_path(self):
        self.color = PATH

    # this is drawing cubes on grib with colors
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        # add upper node
        if self.row > 0 and not grid[self.row - 1][self.col].is_block():
            self.neighbors.append(grid[self.row - 1][self.col])

        # add lower node
        if self.row < len(grid) - 1 and not grid[self.row + 1][self.col].is_block():
            self.neighbors.append(grid[self.row + 1][self.col])

        # add right node
        if self.col < len(grid[0]) - 1 and not grid[self.row][self.col + 1].is_block():
            self.neighbors.append(grid[self.row][self.col + 1])

        # add left node
        if self.col > 0 and not grid[self.row][self.col - 1].is_block():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


# this is a heuristic function which calculates cooridinate distance
# we can change this to Mahhattan distance formula
def h(start, end):
    x1, y1 = start.row, start.col
    x2, y2 = end.row, end.col
    return abs(x1 - x2) + abs(y1 - y2)


# making 2-D list for all nodes on the grid
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
    # initialize the canvas to full white before drawing anything else
    win.fill(EMPTY)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()


# the x, y concept is little confusing, x mean col and y mean row, thus we need to swtich them
def get_pos(pos, rows, width):
    x, y = pos
    length = width // rows
    row, col = x // length, y // length
    return row, col


#we are traversing in reverse order to mark path on top of paths alg visualized (end -> start)
def reconstruct_path(cameFrom, cur, draw):
    while cur in cameFrom:
        cur = cameFrom[cur]
        cur.mark_path()
        draw()


def draw_help(win):
    win.fill(EMPTY)
    font = pygame.font.Font('Arial', 30)
    a_star_text = font.render('A Star Alg', True, black, white)
    # bfs_text = font.render('BFS', True, black, white)
    # dfs_text = font.render('DFS', True, black, white)
    star_textbox = a_star_text.get_rect()
    # bfs_textbox = bfs_text.get_rect()
    # dfs_textbox = dfs_text.get_rect()
    star_textbox.center = (200, 200)
    pygame.display.update()

def a_star(draw, start, end):
    count = 0
    cameFrom = {}
    openSet = PriorityQueue()
    openSet.put((start.f, count, start))
    visit = {start} #this helps us which nodes are currently in openSet 
    start.f = h(start, end)
    start.g = 0
    while not openSet.empty():
        #ensuring we can quit anytime we want
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        cur = openSet.get()[2] # this pops out smallest node in the queue
        visit.remove(cur)
        if cur == end:
            reconstruct_path(cameFrom, cur, draw) #redrawing the final path on top of explored nodes
            end.mark_end()
            start.mark_start()
            return True
        for neigh in cur.neighbors:
            temp_gscore = cur.g + 1 # value one is the weight from one node to the other
            if temp_gscore < neigh.g:
                neigh.g = temp_gscore
                cameFrom[neigh] = cur
                neigh.f = temp_gscore + h(neigh, end)
                if neigh not in visit:
                    visit.add(neigh)
                    count += 1
                    openSet.put((neigh.f,count, neigh))
                    neigh.mark_open()
        draw()

        if cur != start:
            cur.mark_closed()
                    

    return False

def main(win, width, MODE, ALG):
    grid = make_grid(ROWS, width)
    start = None
    end = None
    running = True
    while running:
        if MODE == "RUN":
            draw_all(win, grid, ROWS, width)
        elif MODE == "HELP":
            draw_help(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # check when mouse is clicked. We have to change the node color
            if MODE == "RUN":
                if pygame.mouse.get_pressed()[0]:  # this is left click
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
                elif pygame.mouse.get_pressed()[2]:  # this is right click
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        MODE = "HELP"
                    if event.key == pygame.K_r:
                        start, end = None, None
                        for row in grid:
                            for node in row:
                                node.reset()
                    if event.key == pygame.K_SPACE and start and end and MODE == "RUN":
                        for row in grid:
                            for node in row:
                                node.update_neighbors(grid)
                        if ALG == "a_star":
                            a_star(
                                lambda: draw_all(win, grid, ROWS, width),
                                start,
                                end,
                            )
                        elif ALG == "bfs":
                            bfs(
                                lambda: draw_all(win, grid, ROWS, width),
                                start,
                                end,
                            )
                        elif ALG == "dfs":
                            dfs(
                                lambda: draw_all(win, grid, ROWS, width),
                                start,
                                end,
                            )
            if MODE == "HELP":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        MODE = "RUN"
                    elif event.key == pygame.K_a:
                        ALG = 'a_star'
                    elif event.key == pygame.K_b:
                        ALG = 'bfs'
                    elif event.key == pygame.K_c:
                        ALG = "dfs"



    pygame.quit()


main(WIN, WIDTH, MODE, ALG)
