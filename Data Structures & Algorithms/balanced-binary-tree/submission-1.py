# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return check_balanced(root)[0]

def check_balanced(node):
    if not node:
        return True, 0

    A, B = check_balanced(node.left), check_balanced(node.right)

    if not A[0] or not B[0]:
        return False, None

    if abs(A[1] - B[1]) > 1:
        return False, None

    return True, 1 + max(A[1], B[1])