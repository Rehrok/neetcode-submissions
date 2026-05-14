class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return max(process(nums))

def process(data):
    data.sort()
    count = 1
    for i, x in enumerate(data):
        yield count

        if i == 0 or x == data[i - 1]:
            continue

        if x == data[i - 1] + 1:
            count += 1
            continue

        count = 1

    yield count