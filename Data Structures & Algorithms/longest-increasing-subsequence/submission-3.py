class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return process(nums)


def process(data):
    N = len(data)
    length_at = [0] * N

    for i, x in enumerate(data):
        best_length = 0
        for j, y in enumerate(data[:i]):
            if y < x:
                best_length = max(best_length, length_at[j])
        length_at[i] = best_length + 1

    return max(length_at)