from curses.ascii import isalnum, isdigit

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return process(s)

def process(data):
    for x, y in zip(sequence(data), sequence(data[::-1])):
        if x != y:
            return False
    return True

def sequence(data):
    for x in data:
        if not isalnum(x):
            continue
        
        if isdigit(x):
            yield x

        yield x.lower()       