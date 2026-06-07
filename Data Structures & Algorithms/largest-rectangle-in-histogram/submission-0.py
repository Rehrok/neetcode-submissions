class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return process(heights)

def process(data):
    N = len(data)
    working, result = [], 0

    for i in range(N + 1):
       
        x = data[i] if i < N else float("-inf")
        j = i
        while working and working[-1][1] > x:
            j, y = working.pop()
            result = max(result, y * (i - j))

        working.append((j, x))

    return result