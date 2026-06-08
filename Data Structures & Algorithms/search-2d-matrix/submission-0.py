class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return search_rows(matrix, 0, len(matrix), target)

def search_rows(data, start, end, target):
    N, M = len(data), len(data[0])

    if start >= end:
        return False

    i = start + (end - start) // 2
    a, b = data[i][0], data[i][-1]

    if a <= target <= b:
        return search_col(data[i], 0, M, target)

    return search_rows(data, start, i, target) if target < a \
        else search_rows(data, i + 1, end, target)

def search_col(data, start, end, target):

    if start >= end:
        return False

    i = start + (end - start) // 2
    x = data[i]

    if x == target:
        return True

    return search_col(data, start, i, target) if target < x \
        else search_col(data, i + 1, end, target)