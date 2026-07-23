# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        _, __, lca = process(root, p, q)
        return lca

def process(node, a, b):

    if not node:
        return False, False, None

    found = 0

    if node.val == a.val or node.val == b.val:
        found += 1

    for child in [node.left, node.right]:
        done, partial, result = process(child, a, b)
        if done:
            return done, False, result
        
        if partial:
            found += 1

            if found == 2:
                return True, False, node
    
    return False, found > 0, None        