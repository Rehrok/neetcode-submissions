class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return process(head, n)

def process(node, n):
    dummy = ListNode()
    dummy.next = node
    
    A, B = dummy, dummy

    for _ in range(n):
        B = B.next

    while B.next:
        A, B = A.next, B.next

    A.next = A.next.next

    return dummy.next