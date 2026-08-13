from heapq import heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        return process(stones)

def process(data):
    working = []

    for x in data:
        heappush(working, -1 * x)

    while len(working) > 1:
        x, y = -1 * heappop(working), -1 * heappop(working)
        if x == y:
            continue

        heappush(working, -1 * abs(x - y))

    return -1 * working[0] if working else 0