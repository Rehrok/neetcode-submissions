class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return list(solve(n, set(), set(range(n))))

OPEN = '.'
QUEEN = 'Q'
DIAGONALS = [(-1,-1),(-1,1)]

def build_board(N, placed):
    working = [[OPEN] * N for _ in range(N)]

    for row, col in placed:
        working[row][col] = QUEEN

    return ["".join(x) for x in working]

def check_placement(N, placed, coord):
    for dx, dy in DIAGONALS:
        row, col = coord
        while 0 <= row < N and 0 <= col < N:
            if (row, col) in placed:
                return False
            row, col = row + dx, col + dy

    return True

def solve(N, placed, cols):

    if len(placed) == N:
        yield build_board(N, placed)
        return

    row = len(placed)

    for x in cols:
        coord = (row, x)

        if check_placement(N, placed, coord):
            placed.add(coord)
            yield from solve(N, placed, set(cols) - set([x]))
            placed.remove(coord)