class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return can_balance(nums, 0, 0, set())

def can_balance(data, index, delta, memo):
    N = len(data)

    if index == N:
        return delta == 0

    key = (index, delta)
    if key in memo:
        return False

    x = data[index]
    for dx in [x, -x]:
        if can_balance(data, index + 1, delta + dx, memo):
            return True
    
    memo.add(key)
    return False