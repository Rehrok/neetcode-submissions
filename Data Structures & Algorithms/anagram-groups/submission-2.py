class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return list(process(strs))

def process(data):
    N = len(data)
    i = 0

    while i < N:
        x, X = data[i], hash(data[i])
        a, b = i, i + 1

        for j in range(i + 1, N):
            y, Y = data[j], hash(data[j])

            if X == Y:
                data[b], data[j] = data[j], data[b]
                b += 1

        yield list(data[a:b])
        i = b

def hash(value):
    return "".join(sorted([x for x in value]))