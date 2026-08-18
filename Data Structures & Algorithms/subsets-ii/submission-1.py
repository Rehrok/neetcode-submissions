class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return list(set(process(sorted(nums), 0, [])))

def process(data, index, path):
    if index >= len(data):
        yield tuple(path)
        return

    yield from process(data, index + 1, path)
    path.append(data[index])
    yield from process(data, index + 1, path)
    path.pop()