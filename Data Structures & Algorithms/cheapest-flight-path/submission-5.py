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
    min_stops = {}

    while A:
        path_cost, stops, x = heappop(A)

        if x == end:
            return path_cost

        if x in min_stops and stops + 1 > min_stops[x]:
            continue

        min_stops[x] = stops + 1

        for y, cost in graph[x]:

            if y != end and stops + 1 > K:
                continue

            heappush(A, (path_cost + cost, stops + 1, y))

    return -1