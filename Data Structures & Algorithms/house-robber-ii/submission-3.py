class Solution:
    def rob(self, nums: List[int]) -> int:
        return compute_max_ring(nums)
        
def compute_max(data):
    N = len(data)
    totals = [0] * N

    if N == 0: return 0
    if N == 1: return data[0]

    totals[0] = data[0]
    totals[1] = max(data[0], data[1])

    for i in range(2, N):
        a = data[i] + totals[i - 2]
        b = totals[i - 1]
        totals[i] = max(a, b)

    return totals[-1]

def compute_max_ring(data):

    N = len(data)

    if N == 0: return 0
    if N == 1: return data[0]

    max_total = -math.inf
    
    for i, x in enumerate(data):
        candidate = compute_max(data[i + 1:] + data[:i])
        max_total = max(max_total, candidate)

    return max_total