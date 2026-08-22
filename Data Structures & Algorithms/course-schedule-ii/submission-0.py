from collections import defaultdict

class Graph:
    def __init__(self, vertex_count, edges):
        self.degrees = [0] * vertex_count
        self.connections = [set() for _ in range(vertex_count)]

        for x, y in edges:
            self.degrees[x] += 1
            self.connections[y].add(x)

    def topological_sort(self):
        working = list(self.degrees)
        ordering = []
        A = [i for i, x in enumerate(working) if x == 0]

        while A:
            B = []
            for x in A:
                ordering.append(x)
                for y in self.connections[x]:
                    working[y] -= 1
                    if working[y] == 0:
                        B.append(y)
                        
            A, B = B, A

        return [] if any(working) else ordering

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return Graph(numCourses, prerequisites).topological_sort()
        