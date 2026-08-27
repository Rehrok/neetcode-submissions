class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return process(s, set(wordDict), 0, {})


def process(data, words, index, memo):
    N = len(data)

    if index == len(data):
        return True

    if index in memo:
        return memo[index]
    
    for j in range(index + 1, N+1):
        if data[index:j] in words and process(data, words, j, memo):
            memo[index] = True
            return True

    memo[index] = False
    return False