class Solution:
    def findMin(self, nums: List[int]) -> int:
        return search_min(nums, 0, len(nums))


"""
[3,4,5,6,1,2] -> 1
"""

def search_min(data, start, end):

    i = start + (end - start) // 2
    a, x, b = data[0], data[i], data[-1]

    if a <= x <= b:
        return a

    if end - start <= 2:
        return min(data[start], data[start+1])

    return search_min(data, start + 1, i) if a > x else search_min(data, i, end)