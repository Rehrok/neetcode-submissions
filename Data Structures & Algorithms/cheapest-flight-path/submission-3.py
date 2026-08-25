from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        return compute_min_cost(n, flights, src, dst, k)

def build_graph(data):
    graph = defaultdict(list)

    for x, y, cost in data:
        graph[x].append((y, cost))

    return graph

def compute_min_cost(N, data, start, end, K):
    
    graph = build_graph(data)
    A = [(0, 0, start)]
    costs = { (start, 0) : 0}

    while A:
        path_cost, stops, x = heappop(A)

        if x == end:
            return path_cost

        for y, cost in graph[x]:

            z = path_cost + cost
            key = (y, stops + 1)
            if key in costs and z >= costs[key]:
                continue

            if y != end and stops + 1 > K:
                continue

            costs[key] = z
            heappush(A, (z, stops + 1, y))

    return -1