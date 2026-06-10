# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return process(list1, list2)

def process(A, B):
    dummy = ListNode()
    cursor = dummy

    while A and B:
        if A.val < B.val:
            x, A = A, A.next
        else:
            x, B = B, B.next

        cursor.next, cursor = x, x

    if A:
        cursor.next = A
    if B:
        cursor.next = B

    return dummy.next