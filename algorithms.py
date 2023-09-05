import pygame
from queue import PriorityQueue
from path import *


def a_star(draw,grid, start, end):
    openSet = PriorityQueue()
    closedSet = {}
    cameFrom = {}
    start.g = 0
    start.h = h(start, end)
    openSet.put(start)
    while not openSet.empty():
        #just in case something goes wrong, I can quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        cur = openSet.get()
        if cur == end:
            return reconstruct_path(cameFrom, cur)
        for neighbor in cur.neighbors:
            temp_gScore = neighbor.g + 1 #we are assuming that each path in the grid is cost 1
            if temp_gScore < neighbor.g:
                neighbor.g = temp_gScore
                neighbor.f = temp_gScore + h(neighbor, end)
                cameFrom[neighbor] = cur
                if neighbor not in openSet:
                    openSet.put(neighbor)
                    neighbor.mark_open()
        draw()
        if cur != start:
            cur.mark_closed()

    return False
    


def bfs(draw, grid, start, end):
    pass


def dfs(draw, grid, start, end):
    pass


