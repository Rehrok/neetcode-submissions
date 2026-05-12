class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return process(s, t)

def process(a, b):
    for i in range(ord('a'), ord('z')):
        x = chr(i)
        if count_character(a, x) != count_character(b, x):
            return False
    return True

def count_character(data, target):
    return sum(1 if x == target else 0 for x in data)