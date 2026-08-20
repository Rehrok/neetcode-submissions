from collections import defaultdict

class PrefixNode:
    def __init__(self, is_terminal=False):
        self.is_terminal = is_terminal
        self.connections = defaultdict(PrefixNode)

    def insert(self, data, index):
        if index == len(data):
            self.is_terminal = True
            return

        x = data[index]
        self.connections[x].insert(data, index + 1)

def search(node, data, index, allow_prefix):

    while node:
        if index == len(data):
            return node.is_terminal or allow_prefix

        x = data[index]
        if x in node.connections:
            node, index = node.connections[x], index + 1
        else:
            break

    return False
            
class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()
        
    def insert(self, word: str) -> None:
        self.root.insert(word, 0)

    def search(self, word: str) -> bool:
        return search(self.root, word, 0, False)
        
    def startsWith(self, prefix: str) -> bool:
        return search(self.root, prefix, 0, True)