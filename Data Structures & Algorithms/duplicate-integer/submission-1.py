class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return process(nums)
        
def process(data):
    data.sort()
    for i in range(len(data)):
        if i > 0 and data[i-1] == data[i]:
            return True
    return False