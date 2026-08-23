from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return ladder_distance(build_pattern_to_words(wordList), beginWord, endWord)

def word_to_patterns(word):
    for i in range(len(word)):
        yield word[:i] + '*' + word[i+1:]

def build_pattern_to_words(words):
    pattern_to_words = defaultdict(set)

    for x in words:
        for y in word_to_patterns(x):
            pattern_to_words[y].add(x)

    return pattern_to_words

def ladder_distance(graph, start, end):

    A = [start]
    visited = {start}
    steps = 0

    while A:

        B = []
        for x in A:
    
            if x == end:
                return steps + 1

            for y in word_to_patterns(x):
                for nx in graph[y]:
                    if nx not in visited:
                        visited.add(nx)
                        B.append(nx)
        
        steps, A = steps + 1, B

    return 0