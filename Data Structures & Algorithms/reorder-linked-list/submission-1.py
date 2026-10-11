# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverse_list(head:Optional[ListNode]) -> ListNode:
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        slow.next = None
        second = reverse_list(second)

        first = head
# The idea is, second is being inserted inside first, hence as long as,
# second is present, insert it, and rest remains the same as first list.

        while second:  
            temp1 = first.next
            temp2 = second.next

            first.next = second
            first = temp1

            second.next = first
            second = temp2

        
            



                


                


        
        