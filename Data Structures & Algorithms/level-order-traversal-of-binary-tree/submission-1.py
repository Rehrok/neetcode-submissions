# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return process(root, 0, [])

def process(node, depth, levels):

    if not node:
        return levels

    if len(levels) < depth + 1:
        levels.append([])

    levels[depth].append(node.val)

    process(node.left, depth + 1, levels)
    process(node.right, depth + 1, levels)

    return levels