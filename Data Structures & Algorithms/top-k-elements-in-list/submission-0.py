from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return process(nums, k)

def process(data, k):
    working = Counter(data)
    return [x for x, _ in working.most_common(k)]