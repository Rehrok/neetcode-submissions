class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        return process(target, position, speed)

def process(target, positions, speeds):
    data = sorted([(x,y) for x, y in zip(positions, speeds)], reverse=True)

    slowest_time = float("-inf")
    results = 0

    for x, y in data:
        arrival = (target - x) / y
        if arrival > slowest_time:
            slowest_time, results = max(arrival, slowest_time), results + 1

    return results