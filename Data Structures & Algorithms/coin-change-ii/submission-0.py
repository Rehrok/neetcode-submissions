class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return process(coins, amount, 0, {})

def process(deltas, target, index, memo):

    N = len(deltas)

    if target < 0:
        return 0

    if target == 0:
        return 1

    if index > N:
        return 0

    key = (target, index)
    if key in memo:
        return memo[key]

    result = 0
    for i in range(index, N):
        x = deltas[i]
        result += process(deltas, target - x, i, memo)

    memo[key] = result
    return result