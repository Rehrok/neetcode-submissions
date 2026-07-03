from itertools import zip_longest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return process(p, q)

SENTINEL = 1000

def process(p, q):
    for x, y in zip_longest(traversal(p), traversal(q), fillvalue=SENTINEL):
        if x != y:
            return False

    return True

def traversal(node):
    if node:
        yield node.val
        yield from traversal(node.left)
        yield from traversal(node.right)
    else:
        yield None
        