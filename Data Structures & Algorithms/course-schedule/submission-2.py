from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        counts, connections = build(numCourses, prerequisites)
        return not check_cycle(counts, connections)

def build(course_count, prerequisites):
    counts = [0] * course_count
    connections = defaultdict(list)

    for edge in prerequisites:
        x, y = edge
        connections[y].append(x)
        counts[x] += 1

    return counts, connections


def check_cycle(counts, connections):
    A = list(i for i, x in enumerate(counts) if x == 0)
    while A:
        B = []
        for x in A:
            if x not in connections:
                continue

            for y in connections[x]:
                counts[y] -= 1
                if counts[y] == 0:
                    B.append(y)
        A, B = B, A

    return any(counts)