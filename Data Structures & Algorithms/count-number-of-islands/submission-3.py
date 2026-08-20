DELTAS = ((1, 0), (0, 1), (-1, 0), (0, -1))
WATER = "0"
LAND = "1"

def in_bounds(rows, cols, coord):
    r, c = coord
    return 0 <= r < rows and 0 <= c < cols

def neighbors(coord):
    r, c = coord
    for dr, dc in DELTAS:
        yield (r + dr, c + dc)

def search(grid, coord, visited, rows, cols):
    r, c = coord
    idx = r * cols + c

    if visited[idx]:
        return False

    visited[idx] = 1

    if grid[r][c] != LAND:
        return False

    for nxt in neighbors(coord):
        if in_bounds(rows, cols, nxt):
            search(grid, nxt, visited, rows, cols)

    return True

def count_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = bytearray(rows * cols)
    result = 0

    for r in range(rows):
        for c in range(cols):
            if search(grid, (r, c), visited, rows, cols):
                result += 1

    return result

class Solution:
    def numIslands(self, grid):
        return count_islands(grid)