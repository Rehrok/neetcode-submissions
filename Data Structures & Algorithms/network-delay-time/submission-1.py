from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        return compute_min_time(build_graph(times), n, k - 1)

def build_graph(connections):
    graph = defaultdict(list)

    for x, y, z in connections:
        graph[x - 1].append((y - 1, z))
    
    return graph

def compute_min_time(graph, N, index):
    A = {index}
    times = [math.inf] * N
    times[index] = 0

    while A:
        B = set()

        for x in A:
            for y, dt in graph[x]:
                nt = times[x] + dt
                if nt < times[y]:
                    times[y] = nt
                    B.add(y)
        A, B = B, A

    result = max(times)
    return result if result < math.inf else -1