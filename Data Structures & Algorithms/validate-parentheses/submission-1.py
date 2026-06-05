class Solution:
    def isValid(self, s: str) -> bool:
        return process(s)

OPEN = '([{'
CLOSE = ')]}'
OPEN_TO_CLOSE = { x: y for x, y in zip(OPEN, CLOSE) }

def process(data):
    working = []

    for x in data:
        if x in OPEN_TO_CLOSE:
            working.append(x)
        elif working and OPEN_TO_CLOSE[working[-1]] == x:
            working.pop()
        else:
            return False

    return not working