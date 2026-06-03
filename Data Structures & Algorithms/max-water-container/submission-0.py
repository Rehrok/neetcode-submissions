class Solution:
    def maxArea(self, heights: List[int]) -> int:
        return process(heights)

def process(data):
    result , _, __ =  max(water_sequence(data))
    return result

def water_sequence(data):
    N = len(data)
    i, j = 0, N - 1

    while i < j:
        x, y = data[i], data[j]
        value = min(x, y) * (j - i)
        yield value, i, j

        if x < y:
            i += 1
        else:
            j -= 1