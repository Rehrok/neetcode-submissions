"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return process(head) if head else None

def process(A):
    cursor = A
    
    while cursor:
        x, y = cursor, cursor.next
        x.next = Node(cursor.val, y, cursor.random)
        cursor = y

    cursor = A
    while cursor:
        x, y, z = cursor, cursor.next, cursor.next.next
        y.random = x.random.next if x.random else None
        cursor = z

    B = A.next
    dummy_a, dummy_b = Node(0, A), Node(0, B)

    cursor = A
    while cursor:
        a, b = cursor, cursor.next
        a.next, b.next = b.next, b.next.next if b.next else None
        cursor = a.next

    return dummy_b.next