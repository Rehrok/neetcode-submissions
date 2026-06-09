class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return rot_search(nums, target, 0, len(nums) - 1)

def rot_search(data, target, start, end):

    if start > end:
        return -1

    i = start + (end - start) // 2
    x = data[i]

    if x == target:
        return i

    a, b = data[start], data[end]

    # left is not rotated
    if a <= x:
        in_left = a <= target <= x
        if in_left:
            return rot_search(data, target, start, i)
        else:
            return rot_search(data, target, i + 1, end)

    # then right is not rotated
    else:
        in_right = x <= target <= b
        if not in_right:
            return rot_search(data, target, start, i)
        else:
            return rot_search(data, target, i + 1, end)