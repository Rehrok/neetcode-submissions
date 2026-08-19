class Solution:
    def partition(self, s: str) -> List[List[str]]:
        _, results = process(s, 0, {})

        return results

def process(data, start, memo):
    results = []

    if start == len(data):
        return True, [[]]

    if start in memo:
        return memo[start]

    for i in range(len(data) - start):
        if check(data, start, start + i + 1):

            prefix = [data[start: start + i + 1]]
            ok, suffix = process(data, start + i + 1, memo)

            if ok:
                for x in suffix:
                    results.append(prefix + x)

    ok = len(results) > 0
    memo[start] = ok, results
    return ok, results

def check(data, start, end):

    while start < end:
        if data[start] != data[end - 1]:
            return False
        start, end = start + 1, end - 1

    return True