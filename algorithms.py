from queue import PriorityQueue
from typing import Deque

# def a_star(draw, start, end):
#     count = 0
#     cameFrom = {}
#     openSet = PriorityQueue()
#     openSet.put((start.f, count, start))
#     visit = {start} #this helps us which nodes are currently in openSet 
#     start.f = h(start, end)
#     start.g = 0
#     while not openSet.empty():
#         #ensuring we can quit anytime we want
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#         cur = openSet.get()[2] # this pops out smallest node in the queue
#         visit.remove(cur)
#         if cur == end:
#             reconstruct_path(cameFrom, cur, draw)
#             end.mark_end()
#             return True
#         for neigh in cur.neighbors:
#             temp_gscore = cur.g + 1 # value one is the weight from one node to the other
#             if temp_gscore < neigh.g:
#                 neigh.g = temp_gscore
#                 cameFrom[neigh] = cur
#                 neigh.f = temp_gscore + h(neigh, end)
#                 if neigh not in visit:
#                     visit.add(neigh)
#                     count += 1
#                     openSet.put((neigh.f,count, neigh))
#                     neigh.mark_open()
#         draw()
#
#         if cur != start:
#             cur.mark_closed()
#                     
#
#     return False




def bfs(draw, grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    direction = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    q = []
    visit = set()
    q.append()
    pass

def dfs(draw, grid, start, end):
    pass


