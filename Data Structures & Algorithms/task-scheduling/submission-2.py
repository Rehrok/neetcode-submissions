from heapq import heappush, heappop
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        return process(tasks, n)

def process(data, n):
    heap = []
    time = 0
    queue = deque()

    for key, count in Counter(data).items():
        heappush(heap, (-1 * count, key))

    while heap or queue:
        if heap:
            fitness, task = heappop(heap)
            count = (-1 * fitness) - 1
            if count:
                queue.append((time + n, count, task))

        if queue and queue[0][0] == time:
            _, count, task = queue.popleft()
            heappush(heap, (-1 * count, task))

        time += 1

    return time

    

