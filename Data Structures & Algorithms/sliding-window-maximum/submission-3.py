from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return list(process(nums, k))

def process(data, k):
    working = deque()

    for i, x in enumerate(data):
        while working and working[0][0] < x:
            working.popleft()

        while working and working[-1][0] < x:
            working.pop()

        while working and working[0][1] <= i - k:
            working.popleft()

        working.append((x,i))

        if working and i >= k - 1:
            yield working[0][0]
        


        
