from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return [list(x) for x in set(process(nums))]


def process(data):
    N = len(data)
    value_to_index = defaultdict(list)

    for i, x in enumerate(data):
        value_to_index[x].append(i)

    for i in range(N):
        for j in range(i + 1, N):
            x = data[i] + data[j]
            if -x in value_to_index:
                for k in value_to_index[-x]:
                    if k > j:
                        yield tuple(sorted([data[i], data[j], data[k]]))