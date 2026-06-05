from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return list(process(nums, k))

def process(data, k):
    working = []

    N = len(data)

    for i in range(k):
        heappush(working, (-data[i], i))

    for i in range(N - k + 1):
        while working[0][1] < i:
            A = heappop(working)

        y = working[0][0] * -1
        yield y

        if i + k >= N:
            break

        heappush(working, (-data[i+k], i+k))