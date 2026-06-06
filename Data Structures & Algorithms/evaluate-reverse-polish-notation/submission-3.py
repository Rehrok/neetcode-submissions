class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return process(tokens)

SYMBOL_TO_FN = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: int(a / b),
}
def op(a, b, symbol):
    return SYMBOL_TO_FN[symbol](int(a), int(b))

def process(data):
    working = []

    for x in data:
        if x in SYMBOL_TO_FN:
            b, a = working.pop(), working.pop()
            working.append(op(a, b, x))
        else:
            working.append(x)

    return int(working[-1]) if len(working) == 1 else None