class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return process(nums)

def process(data):

    for i, x in enumerate(data):
        a = abs(x)
        b = data[a]
        if b < 0:
            return a

        data[a] = data[a] * -1