class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return max(compute_areas(grid), default=0)

LAND = 1
DELTAS = [(1,0), (0,1), (-1,0), (0,-1)]

def neighbors(data, coord):
    N, M = len(data), len(data[0])
    row, col = coord

    for a, b in DELTAS:
        if 0 <= row + a < N and 0 <= col + b < M:
            yield row + a, col + b
    
def search(data, coord, visited, current):

    if coord in visited:
        return False, 0

    row, col = coord
    x = data[row][col]

    if x != LAND:
        return False, 0

    visited.add(coord)
    current.add(coord)

    for c in neighbors(data, coord):
        search(data, c, visited, current)

    return True, len(current)

def compute_areas(data):
    N, M = len(data), len(data[0])
    visited = set()

    for row in range(N):
        for col in range(M):
            coord = (row, col)
            found, area = search(data, coord, visited, set())
            if found:
                yield area
