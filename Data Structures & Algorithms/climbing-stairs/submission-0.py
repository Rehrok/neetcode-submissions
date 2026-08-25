class Solution:
    def climbStairs(self, n: int) -> int:
        return process(n)

def process(N):
    data = [0] * (N + 1)
    data[0] = 1
    data[1] = 1

    for i in range(2, N + 1):
        data[i] = data[i - 1] + data[i - 2]

    return data[-1]