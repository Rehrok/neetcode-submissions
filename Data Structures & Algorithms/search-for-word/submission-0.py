class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return check(board, word)

def check(data, target):
    N, M = len(data), len(data[0])

    for i in range(N):
        for j in range(M):
            if search(data, target, i, j, 0, set()):
                return True

    return False

def in_bounds(data, row, col):
    N, M = len(data), len(data[0])
    if 0 <= row < N and 0 <= col < M:
        return True

    return False

def deltas():
    return [(0,1),(1,0),(0,-1),(-1,0)]

def search(data, target, row, col, index, seen):

    if not in_bounds(data, row, col):
        return False

    coord = (row, col)

    if coord in seen:
        return False

    if data[row][col] != target[index]:
        return False

    if index == len(target) - 1:
        return True

    seen.add(coord)

    for a, b in deltas():
        if search(data, target, row + a, col + b, index + 1, seen):
            return True

    seen.remove(coord)
