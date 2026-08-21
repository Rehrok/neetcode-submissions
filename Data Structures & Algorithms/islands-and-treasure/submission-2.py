class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        compute_shortest_distance(grid)

GOAL = 0
BLOCKER = -1
DELTAS = [(1,0), (0,1), (-1,0), (0,-1)]
 
def find_goals(grid):
    N, M = len(grid), len(grid[0])
    for row in range(N):
        for col in range(M):
            if grid[row][col] == GOAL:
                yield (row, col)

def adjacent(grid, coord):
    N, M = len(grid), len(grid[0])
    x, y = coord

    for dx, dy in DELTAS:
        row, col = x + dx, y + dy
        if 0 <= row < N and 0 <= col < M and grid[row][col] != BLOCKER:
            yield (row, col)
       
def compute_shortest_distance(grid):
    A = list(find_goals(grid))
    distance = 1

    while A:
        B = []
        for c in A:
            for row, col in adjacent(grid, c):
                if grid[row][col] > distance:
                    grid[row][col] = distance
                    B.append((row, col))
                
        A, B = B, A
        distance += 1