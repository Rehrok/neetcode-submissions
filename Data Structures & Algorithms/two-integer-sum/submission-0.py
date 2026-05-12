class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return process(nums, target)

def process(data, target):
    for i, x in enumerate(data):
        for j, y in enumerate(data):
            if i != j and x + y == target:
                return [i, j]
        