class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(process(set(nums), []))

def process(pool, path):
    if not pool:
        yield path[::]
        return

    for x in pool:
        remaining = set(pool)
        path.append(x)
        remaining.remove(x)
        yield from process(remaining, path)
        path.pop()