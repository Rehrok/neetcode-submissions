class Solution:
    def trap(self, height: List[int]) -> int:
        return sum(water_values(height))

def water_values(data):
    N = len(data)
    max_forwards = list(max_sequence(data))
    max_backwards = list(max_sequence(reversed(data)))[::-1]
    
    for i in range(1, N - 1):
        a = max_forwards[i - 1]
        b = max_backwards[i + 1]
        x = data[i]
        result = min(a, b) - x
        yield result if result > 0 else 0
    
def max_sequence(data):
    value = -1

    for x in data:
        value = max(value, x)
        yield value