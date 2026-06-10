# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        return process(head)

def process(node):
    dummy = ListNode()
    x, y = split(node)
    y = reverse(y)
    cursor = dummy

    while x and y:
        a, x = x, x.next
        b, y = y, y.next

        cursor.next = a
        a.next = b
        cursor = b

    cursor.next = x or y

def split(node):
    count = 0

    cursor = node

    while cursor:
        cursor, count = cursor.next, count + 1

    count = count // 2
    cursor = node

    while count > 1:
        cursor, count = cursor.next, count - 1

    x, y = cursor, cursor.next
    x.next = None

    return node, y

def reverse(node):
    x, y = node, None

    while x:
        x.next, x, y = y, x.next, x
    
    return y