from math import inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return sum(process(root, []))

def process(node, greatest):

    if not node:
        return

    x = node.val
    great = not greatest or x >= greatest[-1]

    print(x, greatest)

    if great:
        yield 1
        greatest.append(x)

    yield from process(node.left, greatest)
    yield from process(node.right, greatest)

    if great:
        greatest.pop()