class Solution:
    def rob(self, nums: List[int]) -> int:
        return process(nums)

def process(data):
    N = len(data)
    totals = [0] * N

    if N == 0:
        return 0

    totals[0] = data[0]

    for i in range(1, N):
        a = data[i] + totals[i - 2]
        b = totals[i - 1]
        totals[i] = max(a, b)

    return totals[-1]
