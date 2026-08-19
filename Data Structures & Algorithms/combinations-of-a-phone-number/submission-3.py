class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return search(digits, 0, [], [])

DIGIT_TO_CHARS = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz",
}

def search(data, index, path, results):
    if index >= len(data):
        if path:
            results.append("".join(path))
        return results

    x = data[index]
    for y in DIGIT_TO_CHARS[x]:
        path.append(y)
        search(data, index + 1, path, results)
        path.pop()

    return results