# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return process(l1, l2)

def process(A, B):
    dummy = ListNode()
    cursor = dummy
    carry = 0

    while A or B or carry:
        A, a = (A.next, A.val) if A else (None, 0)
        B, b = (B.next, B.val) if B else (None, 0)
        carry, digit = divmod(a + b + carry, 10)
        X = ListNode(digit)
        cursor.next, cursor = X, X

    return dummy.next