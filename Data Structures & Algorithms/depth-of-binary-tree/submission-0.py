# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return depth(root)


def depth(node):
    if not node:
        return 0

    return 1 + max(depth(node.left), depth(node.right))
        