class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return list(solve(n, set(), set(range(n)), set()))

OPEN = '.'
QUEEN = 'Q'

def build_board(N, placed):
    working = [[OPEN] * N for _ in range(N)]

    for row, col in placed:
        working[row][col] = QUEEN

    return ["".join(x) for x in working]

def diagonal_hashes(coord):
    row, col = coord
    return (True, row - col), (False, row + col)

def solve(N, placed, available_cols, claimed_diagonals):

    if len(placed) == N:
        yield build_board(N, placed)
        return

    row = len(placed)

    for x in tuple(available_cols):
        coord = (row, x)
        a, b = diagonal_hashes(coord)

        if a not in claimed_diagonals and b not in claimed_diagonals:
            placed.add(coord)
            available_cols.remove(x)
            claimed_diagonals.add(a)
            claimed_diagonals.add(b)

            yield from solve(N, placed, available_cols, claimed_diagonals)

            placed.remove(coord)
            available_cols.add(x)
            claimed_diagonals.remove(a)
            claimed_diagonals.remove(b)