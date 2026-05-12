class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return process(nums, target)

def process(data, target):
    seen = dict()

    for i, x in enumerate(data):
        y = target - x
        if y in seen:
            return [seen[y], i]
        seen[x] = i

    return False
        