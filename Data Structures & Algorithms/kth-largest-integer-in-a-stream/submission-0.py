from heapq import heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_length, self.heap = k, []

        for x in nums:
            self.add(x)

    def add(self, val: int) -> int:
        
        heappush(self.heap, val)
        
        if len(self.heap) > self.max_length:
            x = heappop(self.heap)

        return self.heap[0]