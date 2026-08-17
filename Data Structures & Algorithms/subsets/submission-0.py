class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return list(process(nums, 0, set()))

def process(data, index, flags):

    n = len(data)

    if index == n:
        yield build_subset(data, flags)
        return

    yield from process(data, index + 1, flags)
    flags.add(index)
    yield from process(data, index + 1, flags)
    flags.remove(index)

def build_subset(data, flags):
    working = []

    for i, x in enumerate(data):
        if i in flags:
            working.append(x)

    return working