from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass(slots=True)
class TrieNode:
    connections: Dict[str, Any] = field(default_factory=dict)
    is_terminal: bool = False

    def add(self, data, index):
        if index == len(data):
            self.is_terminal = True
            return

        x = data[index]
        if x not in self.connections:
            self.connections[x] = TrieNode()
        
        self.connections[x].add(data, index + 1)

    def search(self, data, index, wildcard):
        if index == len(data):
            return self.is_terminal

        x = data[index]

        if x == wildcard:
            for y in self.connections:
                if self.connections[y].search(data, index + 1, wildcard):
                    return True

        if x in self.connections:
            return self.connections[x].search(data, index + 1, wildcard)

        return False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        self.root.add(word, 0)
        
    def search(self, word: str) -> bool:
        return self.root.search(word, 0, '.')