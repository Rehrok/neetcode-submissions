class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return process(nums)
        
def process(data):
    return len(set(data)) != len(data)
        