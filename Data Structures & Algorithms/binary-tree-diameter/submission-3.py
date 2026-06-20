# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return diameter(root)[0] - 1

def diameter(node):
    if not node:
        return 0, 0

    A, B = diameter(node.left), diameter(node.right)
    return max(A[0], B[0], 1 + A[1] + B[1]), 1 + max(A[1], B[1])