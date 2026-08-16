from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return process(nums, k)

def process(data, k):
    working = []

    for x in data:
        heappush(working, x)
        if len(working) > k:
            _ = heappop(working)
    
    return working[0] if working else None