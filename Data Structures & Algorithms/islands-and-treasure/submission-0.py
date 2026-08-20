GOAL = 0
BLOCKER = -1
INF = 2147483647
DELTAS = [(1,0), (0,1), (-1,0), (0,-1)]

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        return compute_shortest_distance(grid)

def find_goals(data):
    results = []

    N, M = len(data), len(data[0])

    for row in range(N):
        for col in range(M):
            if data[row][col] == GOAL:
                results.append((row, col))

    return results

def neighbors(data, coord):
    row, col = coord
    N, M = len(data), len(data[0])

    for a, b in DELTAS:
        x, y = row + a, col + b
        if 0 <= x < N and 0 <= y < M:
            yield (x, y)

def step_bfs(data, coord, edge):

    row, col = coord
    x = data[row][col]

    for c in neighbors(data, coord):        
        a, b = c
        y = data[a][b]

        if y != INF:
            continue

        if x + 1 < y:
            data[a][b] = x + 1
            edge.append((a,b))

def compute_shortest_distance(data):

    edges = [ [x] for x in find_goals(data) ]

    while any(len(x) for x in edges):

        for i in range(len(edges)):
            A = edges[i]
            B = []
            for x in A: 
                step_bfs(data, x, B)
            edges[i] = B
