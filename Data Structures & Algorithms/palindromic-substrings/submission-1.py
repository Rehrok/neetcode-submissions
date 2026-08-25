class Solution:
    def countSubstrings(self, s: str) -> int:
        return sum(process(s))

def process(data):

    N = len(data)

    if N == 0:
        return

    yield 1

    for i in range(1, N):
        yield from subprocess(data, i, i)
        yield from subprocess(data, i - 1, i)

def subprocess(data, left, right):
    N = len(data)

    while left >= 0 and right < N:

        if data[left] != data[right]:
            return

        yield 1
        left, right = left - 1, right + 1