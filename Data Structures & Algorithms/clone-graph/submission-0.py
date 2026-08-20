"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return deep_copy_graph(node) if node else None

def traversal(node, visit, visited):

    if node in visited:
        return

    visited.add(node)
    visit(node)

    for x in node.neighbors:
        traversal(x, visit, visited)

def deep_copy_graph(root):

    old_to_new = dict()

    def fn(x):
        old_to_new[x] = Node(x.val)
    traversal(root, fn, set())

    for x in old_to_new:
        y = old_to_new[x]
        for nx in x.neighbors:
            ny = old_to_new[nx]
            y.neighbors.append(ny)

    return old_to_new[root]
