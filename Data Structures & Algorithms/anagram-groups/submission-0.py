from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return process(strs)

def process(data):
    working = defaultdict(list)

    for x in data:
        working[hash(x)].append(x)

    return list(working.values())

def hash(value):
    return "".join(sorted([x for x in value]))