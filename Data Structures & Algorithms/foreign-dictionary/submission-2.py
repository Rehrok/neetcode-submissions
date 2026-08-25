from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        ok, graph = build_graph(words)
        if ok:
            free = build_free(words, graph)
            ok, order = topo_sort(graph)

        return "" if not ok else "".join(free) + "".join(order)

def edge_for(A, B):

    for x, y in zip(A, B):
        if x == y:
            continue

        return True, False, x, y
    
    return False, len(A) > len(B), None, None

def build_graph(words):
    graph = defaultdict(set)
    for i in range(1, len(words)):
        A, B = words[i - 1], words[i]
        ok, fatal, x, y = edge_for(A, B)
        if fatal:
            return False, None
        if ok:
            graph[x].add(y)

    return True, graph

def build_free(words, graph):
    universal = set()

    for x in words:
        for y in x:
            universal.add(y)
    
    used = set()
    for x in graph:
        used.add(x)
        for y in graph[x]:
            used.add(y)

    return universal - used

def build_indegree(graph):
    indegree = { x: 0 for x in graph }

    for x in graph:
        for y in graph[x]:
            if y not in indegree:
                indegree[y] = 0
            indegree[y] += 1

    return indegree

def topo_sort(graph):
    indegree = build_indegree(graph)
    results = []

    A = [x for x in indegree if indegree[x] == 0]

    while A:
        B = []
        for x in A:
            results.append(x)
            for y in graph[x]:
                indegree[y] -= 1
                if indegree[y] == 0:
                    B.append(y)
        A, B = B, A

    ok = all(indegree[x] == 0 for x in indegree)
    return ok, results if ok else []