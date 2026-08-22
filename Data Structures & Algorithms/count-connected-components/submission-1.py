class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        return len(compute_roots(n, edges))

def find(index, parents):

    stack = []

    while parents[index] != index:
        stack.append(index)
        index = parents[index]

    for i in stack:
        parents[i] = index

    return index

def compute_roots(N, edges):
    parents = list(range(N))

    for x, y in edges:
        parents[find(x, parents)] = find(y, parents)
        
    for i in range(len(parents)):
        parents[i] = find(i, parents)

    return set(parents)