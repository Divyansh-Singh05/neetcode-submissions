# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def count_nodes(head:ListNode) -> int:
            count = 0
            while head:
                head = head.next
                count += 1
            return count
        
        start_n = count_nodes(head) - n
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        for i in range(start_n):
            curr = curr.next
        curr.next = curr.next.next
        
        return dummy.next
