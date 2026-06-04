class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return max(substring_sequences(s))

def substring_sequences(data):
    N = len(data)
    start = 0
    working = set()
    
    for i, x in enumerate(data):
        yield i - start

        while x in working:
            working.remove(data[start])
            start += 1

        working.add(x)

    yield len(data) - start
    