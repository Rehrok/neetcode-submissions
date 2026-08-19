class Solution:
    def partition(self, s: str) -> List[List[str]]:
        _, results = process(s, 0, len(s))

        return results

def process(data, start, end):
    results = []

    if start == end:
        return True, []

    for i in range(end - start):
        if check(data, start, start + i + 1):

            prefix = [data[start: start + i + 1]]
            ok, suffix = process(data, start + i + 1, end)

            if ok:
                if suffix:
                    for x in suffix:
                        results.append(prefix + x)
                else:
                    results.append(prefix)
                    
    return len(results) > 0, results

def check(data, start, end):

    while start < end:
        if data[start] != data[end - 1]:
            return False
        start, end = start + 1, end - 1

    return True

        