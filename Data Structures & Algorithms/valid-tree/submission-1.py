from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        has_cycles = check_cycles(build_graph(edges), 0, seen, set())
        return not has_cycles and len(seen) == n

def build_graph(edges):
    graph = defaultdict(set)

    for x, y in edges:
        graph[x].add(y)
        graph[y].add(x)

    return graph

def check_cycles(graph, index, seen, used):

    if index in seen:
        return True

    seen.add(index)

    for x in graph[index]:
        c = (min(index, x), max(index, x))
        if c in used:
            continue

        used.add(c)
        if check_cycles(graph, x, seen, used):
            return True

    return False