class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return list(process(n, n, ""))

OPEN = "("
CLOSE = ")"

def process(open_count, close_count, path):

    if not open_count and not close_count:
        yield path
        return

    if open_count:
        yield from process(open_count - 1, close_count, path + OPEN)

    if close_count and close_count > open_count:
        yield from process(open_count, close_count - 1, path + CLOSE)