from math import inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return process(root, (-inf, inf))

def process(node, bounds):
    if not node:
        return True

    x = node.val
    min_bound, max_bound = bounds
    if min_bound < x < max_bound:
        return process(node.left, (min_bound, x)) and process(node.right, (x, max_bound))

    return False