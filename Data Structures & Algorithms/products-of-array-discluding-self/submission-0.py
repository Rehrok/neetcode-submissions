from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return list(process(nums))

def process(data):
    zeros = sum(1 if x == 0 else 0 for x in data)

    if zeros == 0:
        yield from process_non_zero(data)
    elif zeros == 1:
        yield from process_single_zero(data)
    else:
        yield from process_multiple_zero(data)

def process_non_zero(data):
    total = prod(data)
    for x in data:
        yield total // x

def process_single_zero(data):
    total = prod(data)
    for i, x in enumerate(data):
        if x != 0:
            yield 0
        else:
            yield prod(data[:i]) * prod(data[i+1:])

def process_multiple_zero(data):
     for _ in data:
        yield 0