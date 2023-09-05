import pygame
import math
from queue import PriorityQueue



WIDTH = 800
ROWS = 40
WIN = pygame.display.set_mode((WIDTH, WIDTH))
ALG = "a_star"
# Define colors for different types of nodes
EMPTY = (255, 255, 255)  # this is white
VISIT = (128, 0, 128)  # this is purple
OBS = (0, 0, 0)  # this is black
END = (5, 13, 255)  # fix this color later
BEGIN = (255, 0, 0)  # this is red color
PATH = (200, 100, 40)
MODE = "RUN"
pygame.display.set_caption("Path Finding Algorithm")


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

def reconstruct_path(cameFrom, cur, draw):
    pass


def draw_help(win):
    win.fill(EMPTY)
    pygame.display.update()



# def a_star(draw, start, end):
#     openSet = PriorityQueue()
#     visited = {start}
#     cameFrom = {}
#     start.g = 0
#     start.f = h(start, end)
#     openSet.put((start.f, start))
#     while not openSet.empty():
#         #just in case something goes wrong, I can quit
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#         cur = openSet.get()[1]
#         visited.remove(cur)
#         if cur == end:
#             #redraw end node over the path for clarity
#             end.mark_end()
#             return reconstruct_path(cameFrom, cur,draw)
#         for neighbor in cur.neighbors:
#             temp_gScore = cur.g + 1 #we are assuming that each path in the grid is cost 1
#             if temp_gScore < neighbor.g:
#                 neighbor.g = temp_gScore
#                 neighbor.f = temp_gScore + h(neighbor, end)
#                 cameFrom[neighbor] = cur
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     openSet.put((neighbor.f, neighbor))
#                     neighbor.mark_open()
#         draw()
#         if cur != start:
#             cur.mark_closed()
#
#     return False

def a_star(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start, end)

	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from, end, draw)
			end.mark_end()
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor, end)
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.mark_open()

		draw()

		if current != start:
			current.mark_closed()

	return False



def dfs(draw, start, end):
    pass

def bfs(draw, start, end):
    pass


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
                    if event.key == pygame.K_SPACE and start and end and MODE == "RUN":
                        for row in grid:
                            for node in row:
                                node.update_neighbors(grid)
                        if ALG == "a_star":
                            a_star(
                                lambda: draw_all(win, grid, ROWS, width),
                                grid,
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
