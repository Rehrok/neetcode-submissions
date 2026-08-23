from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = build_graph(tickets)
        available = set(range(len(tickets)))
        path = []
        build_path(graph, "JFK", available, path)
        return path[::-1]

def build_graph(tickets):
    graph = defaultdict(list)

    for i, (x, y) in enumerate(tickets):
        graph[x].append((y, i))

    for x in graph:
        graph[x].sort()

    return graph

def build_path(graph, current, available, path):

    for x, i in graph[current]:

        if not i in available:
            continue

        available.remove(i)
        build_path(graph, x, available, path)

    path.append(current)