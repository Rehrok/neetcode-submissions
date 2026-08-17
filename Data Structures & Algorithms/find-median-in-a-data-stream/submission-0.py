from heapq import heappush, heappop
from math import inf


class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []
        

    def addNum(self, num: int) -> None:
        a = self.left[0][1] if self.left else math.inf

        if num < a:
            heappush(self.left, (-num, num))
        else:
            heappush(self.right, (num, num))

        if len(self.left) > len(self.right) + 1:
            _, x = heappop(self.left)
            heappush(self.right, (x, x))

        if len(self.left) < len(self.right):
            _, x = heappop(self.right)
            heappush(self.left, (-x, x))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.left[0][1] + self.right[0][1]) / 2.0
        
        return float(self.left[0][1])