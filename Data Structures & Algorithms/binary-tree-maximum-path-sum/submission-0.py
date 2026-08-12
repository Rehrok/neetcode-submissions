from math import inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result, _ = process(root)
        return result

def process(node):

    if not node:
        return -inf, -inf

    full_a, partial_a = process(node.left)
    full_b, partial_b = process(node.right)

    partial = max(node.val, node.val + partial_a, node.val + partial_b)
    full = max(full_a, full_b, partial, partial_a + node.val + partial_b)

    return full, partial