class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return process(nums, target)

def process(data, target):
    data = sorted([(x, i) for i, x in enumerate(data)])
    i, j = 0, len(data) - 1

    while i < j:
        x = data[i][0] + data[j][0]

        if x == target:
            return sorted([data[i][1], data[j][1]])
        elif x < target:
            i += 1
        else:
            j -= 1

    return False
        