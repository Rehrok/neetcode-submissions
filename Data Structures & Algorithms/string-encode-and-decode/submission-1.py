"""
number of strings (N)
characters per string (M)
"""

"""
characters:string:
"""

PREFIX_DIV = ':'
INTERVAL_DIV = ','
PREFIX_END = '|'


class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(x) for x in encode_sequence(strs))

    def decode(self, s: str) -> List[str]:
        prefix, suffix = build_prefix_suffix(s)
        if not prefix:
            return []
        return list(word_sequence(suffix, interval_sequence(prefix)))

def encode_sequence(data):
    i = 0

    for k, x in enumerate(data):
        if k != 0:
            yield PREFIX_DIV

        j = i + len(x)
        yield i
        yield INTERVAL_DIV
        yield j
        
        i = j

    yield PREFIX_END
    for x in data:
        yield x

def build_prefix_suffix(data):
    i = data.find(PREFIX_END)
    return data[:i], data[i+1:]

def interval_sequence(prefix):        
    for part in prefix.split(PREFIX_DIV):
        a, b = part.split(INTERVAL_DIV)
        yield (int(a), int(b))

def word_sequence(suffix, intervals):
    for i, j in intervals:
        yield suffix[i:j]