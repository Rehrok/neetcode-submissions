from math import inf

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return process(nums)

def process(data):
   
    N = len(data)
    if N == 0: return 0

    max_value, min_value = 1, 1
    result = -math.inf

    for x in data:
        max_value, min_value = max(max_value * x, min_value * x, x), \
            min(max_value * x, min_value * x, x)
        result = max(result, max_value)

    return result