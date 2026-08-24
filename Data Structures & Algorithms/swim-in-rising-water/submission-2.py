from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        return compute_min_time(grid, (0, 0), (N - 1, M - 1))

DELTAS = [(1,0),(0,1),(-1,0),(0,-1)]

def find(parents, x):
    stack = []

    while parents[x] != x:
        stack.append(x)
        x = parents[x]

    for y in stack:
        parents[y] = x
    
    return x

def adjacent(grid, time, coord):
    N, M = len(grid), len(grid[0])
    x, y = coord
    for dx, dy in DELTAS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] <= time:
                yield nx, ny

def union(parents, grid, time, x):
    for y in adjacent(grid, time, x):
        px, py = find(parents, x), find(parents, y)
        if px != py:
            parents[px] = py

def build_heap(grid):
    N, M = len(grid), len(grid[0])
    heap = []
    for x in range(N):
        for y in range(M):
            heappush(heap, (grid[x][y], (x,y)))

    return heap

def build_parents(grid):
    N, M = len(grid), len(grid[0])
    parents = {}
    for x in range(N):
        for y in range(M):
            parents[(x, y)] = (x, y)

    return parents

def compute_min_time(grid, A, B):
    
    heap = build_heap(grid)
    parents = build_parents(grid)

    while heap:
        time, x = heappop(heap)
        union(parents, grid, time, x)

        if find(parents, A) == find(parents, B):
            return time