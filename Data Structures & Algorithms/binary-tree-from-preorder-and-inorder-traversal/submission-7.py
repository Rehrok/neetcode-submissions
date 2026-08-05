# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        value_to_inorder = {x : inorder.index(x) for x in preorder }

        def build(pre_index, start, end):
            nonlocal value_to_inorder

            
            if pre_index >= len(preorder) or start > end:
                #print('.')
                return None, pre_index

            #print(f"* start {start}, end {end}")

            value = preorder[pre_index]
            #print(f"* pre_index {pre_index}, value {value}")
            node = TreeNode(val=value)
            index = value_to_inorder[value]

            #print(f"** subtrees {start}, {index - 1} | {index + 1}, {end}")

            node.left, i = build(pre_index + 1, start, index - 1)
            node.right, j = build(i, index + 1, end)

            return node, j

        root, _ = build(0, 0, len(inorder) - 1)
        return root