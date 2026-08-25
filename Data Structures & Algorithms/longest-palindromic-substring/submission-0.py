class Solution:
    def longestPalindrome(self, s: str) -> str:
        _, result = max(find_palidromes(s))
        return result

def find_palidromes(data):
    N = len(data)

    yield find_palidrome_substring(data, 0, 0)
    
    for i in range(1, N):
        yield find_palidrome_substring(data, i, i)
        yield find_palidrome_substring(data, i - 1, i)

def find_palidrome_substring(data, left, right):
    N = len(data)

    if data[left] != data[right]:
        return 0, ""

    while left - 1 >= 0 and right + 1 < N \
        and data[left - 1] == data[right + 1]:
        left, right = left - 1, right + 1
    
    return right - left, data[left:right + 1]        