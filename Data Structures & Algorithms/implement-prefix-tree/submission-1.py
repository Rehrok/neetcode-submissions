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

    def search(self, data, index, allow_prefix):
        if index == len(data):
            return self.is_terminal or allow_prefix

        x = data[index]
        if x in self.connections:
            return self.connections[x].search(data, index + 1, allow_prefix)

        return False
            
            
class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()
        
    def insert(self, word: str) -> None:
        self.root.insert(word, 0)

    def search(self, word: str) -> bool:
        return self.root.search(word, 0, False)
        
    def startsWith(self, prefix: str) -> bool:
        return self.root.search(prefix, 0, True)