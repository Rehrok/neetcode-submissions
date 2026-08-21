class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        return list(compute_flow_union(heights))

DELTAS = [(1,0),(0,1),(-1,0),(0,-1)]

def oceans(data):
    pacific, atlantic = set(), set()

    N, M = len(data), len(data[0])
    for row in range(N):
        for col in range(M):
            if row == 0 or col == 0:
                pacific.add((row, col))
            if row == N - 1 or col == M - 1:
                atlantic.add((row, col))

    return pacific, atlantic

def adjacent(data, coord):
    N, M = len(data), len(data[0])
    x, y = coord
    a = data[x][y]

    for dx, dy in DELTAS:
        row, col = x + dx, y + dy
        if 0 <= row < N and 0 <= col < M:
            b = data[row][col]
            if b >= a:
                yield (row, col)

def compute_extent(data, starting):
    A = list(starting)
    visited = set(starting)

    while A:
        B = []
        for x in A:
            for y in adjacent(data, x):
                if y not in visited:
                    visited.add(y)
                    B.append(y)
        A, B = B, A

    return visited

def compute_flow_union(data):
    pacific, atlantic = oceans(data)
    return compute_extent(data, pacific) & compute_extent(data, atlantic)