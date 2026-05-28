from curses.ascii import isalnum, isdigit

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return process(s)

def process(data):
    N = len(data)
    for X, Y in zip(sequence(data), sequence(data[::-1])):
        i, x = X
        j, y = Y
        if x != y:
            return False
        if i > N or j > N:
            return True
    return True

def sequence(data):
    for i, x in enumerate(data):
        if not isalnum(x):
            continue
        
        if isdigit(x):
            yield i, x

        yield i, x.lower()       