class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return compute_paths(m, n)

def compute_paths(N, M):

    paths_to = [[0] * M for _ in range(N)]
    for i in range(N):
        paths_to[i][0] = 1

    for j in range(M):
        paths_to[0][j] = 1

    for i in range(1, N):
        for j in range(1, M):
            paths_to[i][j] = paths_to[i - 1][j] + paths_to[i][j - 1]

    return paths_to[-1][-1]