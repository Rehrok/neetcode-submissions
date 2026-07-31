# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return build_tree(preorder, inorder)

def rank(order, value):
    return order.index(value)

def sample(data, index):
    if index < 0 or index >= len(data):
        return None
    return data[index]

def find_left_value(inorder, i, seen):
    #print('* find left')
    while i > 0:
        i -= 1
        #print('- check ', inorder[i])
        if inorder[i] in seen:
            return inorder[i]

def find_right_value(inorder, i, seen):
    #print('* find right')
    while i < len(inorder) - 1:
        i += 1
        #print('- check ', inorder[i])
        if inorder[i] in seen:
            return inorder[i]

def build_tree(preorder, inorder):

    nodes = [TreeNode(x) for x in preorder]
    seen = set()

    for i, x in enumerate(preorder):
        seen.add(x)
        j = rank(inorder, x)

        #print("** visit", x)

        y = find_right_value(inorder, j, seen)
        if y:
            k = rank(preorder, y)
            if not nodes[k].left:
                nodes[k].left = nodes[i]
                #print("*** attach left", y)
                continue
      
        y = find_left_value(inorder, j, seen)
        if y:
            k = rank(preorder, y)
            if not nodes[k].right:
                nodes[k].right = nodes[i]
                #print("*** attach right", y)
                continue

    return nodes[0]