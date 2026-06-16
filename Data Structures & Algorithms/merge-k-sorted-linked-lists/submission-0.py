from heapq import heappush, heappop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return process(lists)

def sequence(node, index):
    while node:
        yield True, node.val, index
        node = node.next
    
    yield False, None, None

def process(data):
    dummy = ListNode()
    cursor = dummy
    working = []

    for i, x in enumerate(data):
        seq = iter(sequence(x, i))
        ok, value, index = next(seq)
        if ok:
            heappush(working, (value, index, seq))

    while working:
        value, index, seq = heappop(working)
        
        cursor.next = ListNode(value)
        cursor = cursor.next

        ok, value, index = next(seq)
        if ok:
            heappush(working, (value, index, seq))

    return dummy.next