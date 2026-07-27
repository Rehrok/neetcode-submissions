# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return process(root, 0, [])

def process(node, depth, results):
    if not node:
        return results

    if depth >= len(results):
        results.append(node.val)
    
    process(node.right, depth + 1, results)
    process(node.left, depth + 1, results)

    return results