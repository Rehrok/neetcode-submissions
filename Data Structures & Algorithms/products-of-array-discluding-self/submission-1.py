class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return list(process(nums))

def process(data):
    N = len(data)
    suffix = build_suffix(data)

    prefix = 1
    for i, x in enumerate(data):
        y = 1 if i == N - 1 else suffix[i + 1]
        yield prefix * y
        prefix *= x

def build_suffix(data):
    N = len(data)
    result = [None] * (N + 1)
    result[N] = 1

    for i in range(N - 1, -1, -1):
        x = result[i + 1]
        result[i] = data[i] * x

    return result