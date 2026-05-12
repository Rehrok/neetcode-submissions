from collections import Counter 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return process(s, t)

def process(a, b):
    return Counter(a) == Counter(b)
        