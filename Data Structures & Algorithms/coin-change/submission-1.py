class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        ok, result = process(sorted(coins, reverse=True), amount, {})
        return result if ok else -1

def process(deltas, target, memo):

    if not deltas:
        return False, -1

    if target == 0:
        return True, 0

    if target < 0:
        return False, -1

    if target in memo:
        return memo[target]

    result = math.inf

    for x in deltas:
        ok, count = process(deltas, target - x, memo)
        if ok:
            result = min(result, count + 1)

    memo[target] = result < math.inf, result
    return memo[target]