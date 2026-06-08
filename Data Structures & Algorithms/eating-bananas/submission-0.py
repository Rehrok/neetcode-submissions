class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return search_speed(piles, h)

def search_speed(data, limit):
    a, b = 1, max(data)

    while a < b:
        x = a + (b - a) // 2
        ok = check_speed(data, limit, x)
        if ok:
            b = x
        else:
            a = x + 1

    return b

def check_speed(data, limit, speed):
    result = sum(math.ceil(x / speed) for x in data)
    return result <= limit