# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

NONE_SENTINEL = '.'
SEPARATOR_SENTINEL = ','

class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        working = []
        build_tree_traversal(root, working)
        return SEPARATOR_SENTINEL.join(working)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        working = data.split(SEPARATOR_SENTINEL)
        result, _ = consume_tree_traversal(working, 0)
        return result

def build_tree_traversal(node, working):
    if node:
        working.append(str(node.val))
        build_tree_traversal(node.left, working)
        build_tree_traversal(node.right, working)
    else:
        working.append(NONE_SENTINEL)
    
def consume_tree_traversal(working, index):
    value_str = working[index]
    if value_str == NONE_SENTINEL:
        return None, index + 1

    else:
        node = TreeNode(int(value_str))
        node.left, i = consume_tree_traversal(working, index + 1)
        node.right, j = consume_tree_traversal(working, i)
        return node, j