class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return compute_max_profit(prices, math.inf, 0, {})

def compute_max_profit(data, cost, index, memo):
    N = len(data)

    if index >= N:
        return 0

    key = (index, cost)
    if key in memo:
        return memo[key]

    x = data[index]
    profit = x - cost

    a = profit + compute_max_profit(data, math.inf, index + 2, memo)
    b = compute_max_profit(data, min(cost, x), index + 1, memo)
    result = max(a, b)

    memo[key] = result
    return result