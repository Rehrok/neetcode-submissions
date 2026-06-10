# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return process(head)

def process(node):
    x, y = node, None

    while x:
        x.next, x, y = y, x.next, x

    return y