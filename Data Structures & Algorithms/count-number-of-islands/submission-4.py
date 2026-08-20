DELTAS = ((1, 0), (0, 1), (-1, 0), (0, -1))
LAND = "1"

def dfs(r, c, grid, visited, rows, cols):
    visited[r * cols + c] = 1
    for dr, dc in DELTAS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == LAND and not visited[nr * cols + nc]:
                dfs(nr, nc, grid, visited, rows, cols)

class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = bytearray(rows * cols)
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == LAND and not visited[r * cols + c]:
                    islands += 1
                    dfs(r, c, grid, visited, rows, cols)

        return islands