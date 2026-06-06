class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return process(temperatures)


def process(data):
    N = len(data)
    working, results = [], [None] * N

    for i in range(N - 1, -1, -1):
        x = data[i]
        while working and working[-1][0] <= x:
            working.pop()

        results[i] = working[-1][1] - i if working else 0
        working.append((x,i))

    return results