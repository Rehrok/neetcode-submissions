class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        return max(profit_sequence(prices))

def min_sequence(data):
    current = data[0]
    for x in data:
        current = min(current, x)
        yield current

    yield current

def profit_sequence(data):
    a = min_sequence(data)
    _ = next(a)
    for x, y in zip(a, data[1:]):
        yield max(y - x, 0)