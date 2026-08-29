class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return compute_lcs(text1, text2, 0, 0, {})

def compute_lcs(A, B, i, j, memo):
    N, M = len(A), len(B)

    if i >= N or j >= M:
        return 0

    key = (i, j)
    if key in memo:
        return memo[key]

    result = None

    if A[i] == B[j]:
        result = 1 + compute_lcs(A, B, i + 1, j + 1, memo)
    else:
        result = max(compute_lcs(A, B, i + 1, j, memo), \
                     compute_lcs(A, B, i, j + 1, memo))

    memo[key] = result
    return result