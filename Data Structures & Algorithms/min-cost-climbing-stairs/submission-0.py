class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return process(cost)

def process(cost_per_step):
    N = len(cost_per_step)
    min_cost = [0] * (N + 1)

    min_cost[0] = 0
    min_cost[1] = 0

    for i in range(2, N + 1):
        min_cost[i] = min(min_cost[i - 2] + cost_per_step[i - 2], min_cost[i - 1] + cost_per_step[i - 1])

    return min_cost[-1]