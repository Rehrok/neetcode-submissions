from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return process(points, k)

ORIGIN = [0.0, 0.0]

def fitness(A, B):
    return -1.0 * ((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)

def process(data, k):
    working = []

    for i, x in enumerate(data):
        heappush(working, (fitness(x, ORIGIN), i, x))
        if len(working) > k:
            _ = heappop(working)

    return [x for _, __, x in working]