

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return count_islands(grid)

def count_islands(data):
    visited, result = set(), 0

    for row in range(len(data)):
        for col in range(len(data[0])):
            if search(data, (row, col), visited):
                result += 1

    return result

DELTAS = [(1,0),(0,1),(-1,0),(0,-1)]
WATER = '0'
LAND = '1'

def neighbors(coord):
    row, col = coord
    for a, b in DELTAS:
        yield (row + a, col + b)

def in_bounds(data, coord):
    row, col = coord
    return 0 <= row < len(data) and 0 <= col < len(data[0])

def search(data, coord, visited):
    if coord in visited:
        return False

    visited.add(coord)

    row, col = coord
    x = data[row][col]

    if x != LAND:
        return False

    for c in neighbors(coord):
        if in_bounds(data, c):
            search(data, c, visited)
    
    return True





        