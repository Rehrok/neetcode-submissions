class Solution:
    def solve(self, board: List[List[str]]) -> None:
        compute_capture(board)

SAFE = 'O'
CAPTURED = 'X'
DELTAS = [(1,0),(0,1),(-1,0),(0,-1)]

def adjacent(data, coord):
    N, M = len(data), len(data[0])
    x, y = coord
    for dx, dy in DELTAS:
        row, col = x + dx, y + dy
        if 0 <= row < N and 0 <= col < M:
            if data[x][y] == data[row][col]:
                yield (row, col)

def outer(data):
    N, M = len(data), len(data[0])

    for x in range(N):
        yield (x, 0)
        yield (x, M - 1)

    for x in range(1, M - 1):
        yield (0, x)
        yield (N - 1, x)

def search_safe(data, starting):
    A = list(starting)
    visited = set(A)

    while A:
        B = []
        for x in A:
            for y in adjacent(data, x):
                if y not in visited:
                    visited.add(y)
                    B.append(y)
        A, B = B, A

    return visited

def update_board(data, safe):
    N, M = len(data), len(data[0])
    for x in range(N):
        for y in range(M):
            if (x, y) not in safe:
                data[x][y] = CAPTURED

def compute_capture(data):
    safe = search_safe(data, ((x, y) for x, y in outer(data) if data[x][y] == SAFE))
    update_board(data, safe)
    