from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return max(value_sequence(s, k))

def value_sequence(data, k):
    print(data)
    N = len(data)
    start = 0
    counts = Counter()

    for i, x in enumerate(data):
        counts[x] += 1

        while value_for(counts, k) == 0:
            y = data[start]
            counts[y] -= 1
            start += 1

        yield value_for(counts, k) 

def value_for(counts, k):
    x, cx = counts.most_common(1)[0]
    total = counts.total()
    if cx + k >= total:
        return total
    return 0