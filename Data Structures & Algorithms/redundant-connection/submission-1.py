class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        return search(edges)

def find(x, parents):
    stack = []

    while x != parents[x]:
        stack.append(x)
        x = parents[x]
    
    for y in stack:
        parents[y] = x

    return x

def search(edges):

    vertices = set()
    for x, y in edges:
        vertices.add(x)
        vertices.add(y)

    parents = list(x for x in range(len(vertices) + 1))

    for x, y in edges:
        px, py = find(x, parents), find(y, parents)
        if px != py:
            parents[px] = py
        else:
            return [x, y]