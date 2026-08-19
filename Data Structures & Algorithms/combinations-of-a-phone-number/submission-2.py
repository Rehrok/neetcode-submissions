class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return list(process(digits, 0, []))

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

def process(data, index, path):
    if index >= len(data):
        if path:
            yield "".join(path)
        return

    x = data[index]

    for y in DIGIT_TO_CHARS[x]:
        path.append(y)
        yield from process(data, index + 1, path)
        path.pop()
