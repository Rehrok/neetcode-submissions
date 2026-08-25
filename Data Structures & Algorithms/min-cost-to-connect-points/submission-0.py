class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        return compute_min_cost(points)

def cost(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])
        
def compute_min_cost(points):
    N = len(points)

    available = set(range(1, N))
    costs = [math.inf] * N
    total_cost = 0
    index = 0

    while available:
        A = points[index]
        cost_for_index = math.inf

        for j in available:
            B = points[j]
            costs[j] = min(cost(A ,B), costs[j])

            if costs[j] < cost_for_index:
                index, cost_for_index = j, costs[j]

        available.remove(index)
        total_cost += cost_for_index

    return total_cost