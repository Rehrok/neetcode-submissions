DELTAS = [(1,0), (0,1), (-1,0), (0,-1)]

class TrieNode:
    __slots__ = ("connections", "handle")

    def __init__(self):
        self.connections = {}
        self.handle = -1

    def add(self, data, index, handle):
        if index >= len(data):
            self.handle = handle
            return

        x = data[index]
        if x not in self.connections:
            self.connections[x] = TrieNode()

        self.connections[x].add(data, index + 1, handle)


    @property
    def is_word(self):
        return self.handle != -1

    def step(self, value):
        if value not in self.connections:
            return None
        return self.connections[value]

def in_bounds(board, coord):
    return 0 <= coord[0] < len(board) and 0 <= coord[1] < len(board[0])

def adjacent(board, coord):
    row, col = coord
    for a, b in DELTAS:
        c = (row + a, col + b)
        if in_bounds(board, c):
            yield c

def search(node, board, coord, visited, found):
    if coord in visited:
        return

    row, col = coord
    x = board[row][col]
    node = node.step(x)

    if not node:
        return

    visited.add(coord)

    if node.is_word:
        found.add(node.handle)

    for c in adjacent(board, coord):
        search(node, board, c, visited, found)

    visited.remove(coord)
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i, x in enumerate(words):
            root.add(x, 0, i)

        handles = set()
        N, M = len(board), len(board[0])
        for row in range(N):
            for col in range(M):
                search(root, board, (row, col), set(), handles)

        return list(words[i] for i in handles)