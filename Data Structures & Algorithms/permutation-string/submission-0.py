from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return process(s1, s2)

def process(a, b):
    A = Counter(a)
    N, M = len(a), len(b)
    B = Counter(b[:N])

    for i, x in enumerate(b):
        if A == B:
            break

        j = i + N
        if j >= M:
            break
        
        y = b[j]
        B[x] -= 1
        B[y] += 1

    return A == B