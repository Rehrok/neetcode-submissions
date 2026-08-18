from collections import defaultdict

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return list(list(x) for x in set(process(sorted(nums), target, 0, 0, defaultdict(int))))

def process(data, target, index, partial, counts):

    if partial == target:
        yield build_combination(data, counts)
        return

    if index >= len(data):
        return

    yield from process(data, target, index + 1, partial, counts)

    x = data[index]

    while partial < target:
        partial += x
        counts[index] += 1
        yield from process(data, target, index + 1, partial, counts)

    counts[index] = 0

def build_combination(data, counts):
    working = []
    for key, value in counts.items():
        for _ in range(value):
            working.append(data[key])

    return tuple(x for x in working)