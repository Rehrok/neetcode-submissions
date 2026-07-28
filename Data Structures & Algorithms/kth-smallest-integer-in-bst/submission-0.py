# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return kth_value(root, k)

def in_order_sequence(node):
    if not node:
        return

    yield from in_order_sequence(node.left)
    yield node.val
    yield from in_order_sequence(node.right)

def kth_value(node, k):
    for i, x in enumerate(in_order_sequence(node)):
        if i + 1 == k:
            return x