from math import inf

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return compute_edit_distance(word1, word2)
 
def compute_edit_distance(A, B):

    N, M = len(A), len(B)

    table = [[0] * (M + 1) for _ in range(N  + 1)]
    for i in range(N + 1):
        table[i][0] = i

    for j in range(M + 1):
        table[0][j] = j

    for i in range(1, N+1):
        for j in range(1, M+1):
            x, y = A[i - 1], B[j - 1]
            table[i][j] = min(
                math.inf if x != y else table[i - 1][j - 1],
                1 + table[i][j - 1],
                1 + table[i -1][j],
                1 + table[i - 1][j - 1],
            )

    return table[-1][-1]