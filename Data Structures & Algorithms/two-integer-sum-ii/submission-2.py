class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = process(numbers, target)
        return [result[0] + 1, result[1] + 1]

# in this case, we should have skipped the secondary while loops
# avoiding the duplicate checks was slower then performing the checks, due to the loop overhead
# note, depending on the cost of the check this is not always the case.

def process(data, target):
    N = len(data)
    i, j = 0, len(data) -1

    while i < j:
        x, y = data[i], data[j]
        current = x + y
        if current == target:
            return [i, j]
        
        if current < target:
            while i < N and data[i] == x:
                i += 1
            continue
        else:
            while j > 0 and data[j] == y:
                j -= 1
            continue

    return None