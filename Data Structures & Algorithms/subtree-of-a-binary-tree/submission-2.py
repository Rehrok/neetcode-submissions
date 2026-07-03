# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return process(root, subRoot, True)

def process(node, target, is_root):
    
    if not target and not node:
        return True

    if not node or not target:
        return False

    if node.val != target.val and not is_root:
        return False

    if node.val == target.val:
        if process(node.left, target.left, False) and process(node.right, target.right, False):
            return True
    
    return process(node.left, target, True) or process(node.right, target, True)