from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        _, __, result = min(process(s, t), default=(0,0,""))
        return result

def process(a, b):
    B = Counter(b)
    A, requires = Counter(), set(B)
    start = 0

    for i, x in sequence(a, B):
        A[x] += 1
        if x in requires and A[x] >= B[x]:
            requires.remove(x)

        while not requires:
            yield (i - start + 1, i, a[start:i+1])

            y, start = a[start], start + 1
            if y in A:
                A[y] -= 1
                if A[y] < B[y]:
                    requires.add(y)
            
def sequence(a, B):
    for i, x in enumerate(a):
        if x in B:
            yield (i, x)

