# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return diameter(root) - 1

def depth(node):
    if not node:
        return 0
    return 1 + max(depth(node.left), depth(node.right))

def diameter(node):
    if not node:
        return 0

    return max(1 + depth(node.left) + depth(node.right), diameter(node.left), diameter(node.right))