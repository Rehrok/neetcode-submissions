class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return rot_search(nums, target, 0, len(nums) - 1)

def fmt(data, start, end):
    return list(str(x) if start <= i <= end else '.' for i, x in enumerate(data))

def rot_search(data, target, start, end):

    if start > end:
        print('failed', start, end)
        return -1

    print(fmt(data, start, end))

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