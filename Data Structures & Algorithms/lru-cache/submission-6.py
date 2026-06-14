class ListNode:

    def __init__(self, key=None, value: int = 0):
        self.key, self.value, self.forward, self.back = key, value, None, None

    def insert_after(self, head):
        x = head.forward
        head.forward, self.back = self, head
        self.forward = x
        if x:
            x.back = self

    def remove_before(self):
        return self.back.cut()
        
    def cut(self):
        self.back.forward, self.forward.back = self.forward, self.back
        self.back, self.forward = None, None
        return self

class LRUCache:

    def __init__(self, capacity: int):
        self.head, self.tail = ListNode(), ListNode()
        self.head.forward, self.tail.back = self.tail, self.head
        self.key_to_node = dict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key].cut()
            node.insert_after(self.head)
            return node.value

        return - 1
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key].cut()
            node.value = value
        else:
            node = ListNode(key, value)
            if len(self.key_to_node) == self.capacity:
                x = self.tail.remove_before()
                del self.key_to_node[x.key]

        node.insert_after(self.head)
        self.key_to_node[key] = node