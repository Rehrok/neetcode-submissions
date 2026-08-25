from heapq import heappush, heappop

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
    A = [(0, 0, start, {start})]

    while A:
        path_cost, stops, x, path_visits = heappop(A)

        if x == end:
            return path_cost

        for y, cost in graph[x]:

            if y in path_visits:
                continue

            if y != end and stops + 1 > K:
                continue

            heappush(A, (path_cost + cost, stops + 1, y, path_visits | {y}))

    return -1