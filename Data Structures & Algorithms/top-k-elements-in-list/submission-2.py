from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return process_counts(count_sequence(nums), k)

def count_sequence(data):
    data.sort()
    value, index = data[0], 0
    for i in range(1, len(data) + 1):
        if i >= len(data) or data[i] != value:
            yield (i - index, index, value)
        
        if i < len(data) and data[i] != value:
            value, index = data[i], i

def process_counts(sequence, k):
    working = []
    for x in sequence:
        heappush(working, x)
        if len(working) > k:
            heappop(working)

    return [x for _, __, x in working]