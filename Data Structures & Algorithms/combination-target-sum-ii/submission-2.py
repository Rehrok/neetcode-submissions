from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        data = Counter(candidates)
        return list(process(sorted(data.keys()), target, 0, 0, [], data))

def process(data, target, index, partial, parts, limits):

    if partial > target:
        return

    if partial == target:
        yield parts[::]
        return

    if index >= len(data):
        return

    yield from process(data, target, index + 1, partial, parts, limits)

    x = data[index]
    count = 0

    for _ in range(limits[x]):
        partial += x
        parts.append(x)
        count += 1
        if partial > target:
            break
        yield from process(data, target, index + 1, partial, parts, limits)

    for _ in range(count):
        parts.pop()