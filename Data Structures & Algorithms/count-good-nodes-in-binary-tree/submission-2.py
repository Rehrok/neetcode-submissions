# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        results = 0

        def process(node, greatest):
            nonlocal results

            if not node:
                return
            x = node.val
            great = not greatest or x >= greatest[-1]

            if great:
                results += 1
                greatest.append(x)

            process(node.left, greatest)
            process(node.right, greatest)

            if great:
                greatest.pop()

        process(root, [])
        return results