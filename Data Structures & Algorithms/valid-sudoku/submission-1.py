DOT = '.'

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return check_board(board)

def check_board(data):
    for i in range(len(data)):
        if not is_valid(row(data, i)):
            return False
        if not is_valid(col(data, i)):
            return False
        if not is_valid(square(data, i)):
            return False
    return True

def row(data, i):
    for x in data[i]:
        yield x

def col(data, i):
    for j in range(len(data)):
        yield data[j][i]

def square(data, i):
    u, v = (i // 3) * 3, (i % 3) * 3
    for i in range(3):
        for j in range(3):
            yield data[u + i][v + j]

def is_valid(sequence):
    seen = set()
    for x in sequence:
        if x == DOT:
            continue
        if x in seen:
            return False
        seen.add(x)
    return True