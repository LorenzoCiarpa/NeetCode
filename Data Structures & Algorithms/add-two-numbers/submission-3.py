# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rest = 0
        head = prev = ListNode(None, None)
        while l1 and l2:
            elem = l1.val + l2.val + rest

            rest = 0
            if elem >= 10:
                elem -= 10
                rest = 1

            
            node = ListNode(elem)
            if prev.val is None:
                prev.val = node.val
            else:
                prev.next = node
                prev = prev.next

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            elem = l1.val + rest
            rest = 0
            if elem >= 10:
                elem -= 10
                rest = 1

            node = ListNode(elem)
            if prev.val is None:
                prev.val = node.val

            else:
                prev.next = node
                prev = prev.next

            l1 = l1.next

        while l2:
            elem = l2.val + rest
            rest = 0
            if elem >= 10:
                elem -= 10
                rest = 1

            node = ListNode(elem)
            if prev.val is None:
                prev.val = node.val
            else:
                prev.next = node
                prev = prev.next

            l2 = l2.next
        
        if rest:
            node = ListNode(rest)
            prev.next = node

        return head
