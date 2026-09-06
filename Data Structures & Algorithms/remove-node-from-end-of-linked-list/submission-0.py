# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def aux(node):
            if not node:
                return None, 1
            
            result = aux(node.next)
            node.next = result[0]

            if result[1] == n:
                return (node.next, result[1] + 1)

            return (node, result[1] + 1)
            
        head, _ = aux(head)
        return head