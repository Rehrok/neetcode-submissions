class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        return process(nums1, nums2)

def value(data, index):
    if index < 0:
        return float("-inf")
    if index >= len(data):
        return float("inf")
    return data[index]

def median(ax, bx, ay, by, N, M):
    c = max(ax, bx)
    d = min(ay, by)

    if (N + M) % 2 == 0:
        return (c + d) / 2
    
    return d

def process(A, B):
    if len(B) < len(A):
        A, B = B, A

    N, M = len(A), len(B)
    H = (N + M) // 2

    start, end = 0, N

    while start <= end:

        i = start + (end - start) // 2
        j = H - i

        ax, bx = value(A, i - 1), value(B, j - 1)
        ay, by = value(A, i), value(B, j)

        if ax <= by and bx <= ay:
            return median(ax, bx, ay, by, N, M)

        if ax > by:
            end = i - 1
        elif bx > ay:
            start = i + 1