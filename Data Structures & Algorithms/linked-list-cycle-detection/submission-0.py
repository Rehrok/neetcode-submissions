# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return process(head)

def process(data):
    A, B = data, data

    while True:

        if not B or not B.next:
            return False

        A, B = A.next, B.next.next
        
        if A == B:
            return True