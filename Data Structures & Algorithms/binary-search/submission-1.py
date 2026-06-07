class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target, 0, len(nums))

def binary_search(data, target, start, end):
    if start >= end:
        return -1

    i = start + (end - start) // 2
    x = data[i]

    if x == target:
        return i

    return binary_search(data, target, start, i) if target < x else binary_search(data, target, i + 1, end)