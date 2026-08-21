class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        return compute_steps(grid)

FRESH, ROTTEN = 1, 2
DELTAS = [(1,0), (0,1), (-1,0), (0,-1)]

def adjacent(data, coord):
    N, M = len(data), len(data[0])
    x, y = coord

    for dx, dy in DELTAS:
        row, col = x + dx, y + dy
        if 0 <= row < N and 0 <= col < M and data[row][col] == FRESH:
            yield (row, col)

def find(data, target):
    N, M = len(data), len(data[0])
    for row in range(N):
        for col in range(M):
            if data[row][col] == target:
                yield (row, col)

def compute_steps(data):
    A = list(find(data, ROTTEN))
    steps = 0

    while A:
        B = []
        for c in A:
            for row, col in adjacent(data, c):
                data[row][col] = ROTTEN
                B.append((row, col))
        if B:
            steps += 1
        A, B = B, A

    return -1 if any(find(data, FRESH)) else steps