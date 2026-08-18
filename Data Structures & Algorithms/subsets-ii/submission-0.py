class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return list(list(x) for x in set(tuple(x) for x in process(sorted(nums), 0, [])))

def process(data, index, path):
    if index >= len(data):
        yield path[::]
        return

    yield from process(data, index + 1, path)
    path.append(data[index])
    yield from process(data, index + 1, path)
    path.pop()