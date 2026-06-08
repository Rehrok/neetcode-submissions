class Solution:
    def findMin(self, nums: List[int]) -> int:
        return search_min(nums, 0, len(nums) - 1)

def search_min(data, start, end):
    if start == end:
        return data[start]

    a, b = data[start], data[end]

    if a < b:
        return a

    i = start + (end - start) // 2
    x = data[i]

    return search_min(data, start, i) if x < b else search_min(data, i + 1, end)