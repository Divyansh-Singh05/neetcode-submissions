# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def listToNum (node : ListNode)  -> int:
            num = node.val
            place = 1
            while node.next:
                node = node.next
                place*=10
                num = num + node.val*place
            return num

        num = listToNum(l1) + listToNum(l2)
        dummy = ListNode(0)
        head = dummy
        
        while num:
            head.next = ListNode(num%10)
            num = num//10
            head = head.next

        if dummy.next is None:
            dummy.next = ListNode(0)

        return dummy.next



